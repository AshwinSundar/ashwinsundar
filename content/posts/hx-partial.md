+++
title = "Two Ways to Render Toasts 🍞"
date = 2026-10-01
genres = ["technical"]
draft = false
+++

MouseHouse implements in-app notifications using the Django messages framework and an htmx v2 [out-of-band swap](https://htmx.org/attributes/hx-swap-oob/). The goal here was to implement [pop-up (a.k.a. "toast") notifications](https://en.wikipedia.org/wiki/Pop-up_notification) in an informative and easy-to-implement manner that would be minimally-annoying to the end user. [Django message framework](https://docs.djangoproject.com/en/6.1/ref/contrib/messages/) is built for this use-case:

> Quite commonly in web applications, you need to display a one-time notification message (also known as “flash message”) to the user after processing a form or some other types of user input.

I'll explain how to implement toast notifications with Django messages and `hx-swap-oob` - and then show you a way to skip Django messages altogether, thanks to the arrival of `hx-partial` in htmx 4.

## Full page loads

To trigger a notification, first [configure Django messages](https://docs.djangoproject.com/en/6.1/ref/contrib/messages/#configuring-the-message-engine) in your Django app. Then, create a `message` in your endpoint. This message gets stapled to your session[^message-attach], and now you have access to the message (via the session object) which you can then render them somewhere in your template:

```python
# views.py
def index(request: HttpRequest) -> HttpResponse:
    messages.success(request, message="Welcome to MouseHouse!", extra_tags="Welcome!")
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))
```

```htmldjango
<!--toasts-container.html-->
<div class="flex flex-col space-y-3 fixed z-30 bottom-4 right-3">
  {% for message in messages %}
    {% include "partials/toast.html" %}
  {% endfor %}
</div>
```

With a little styling, the `toasts-container` is fixed to the bottom right of the page. Messages are cleared automatically once the client processes the request[^message-expiration].

## Handling partial responses

What if the whole page isn't being reloaded, such as in the case of a [partial response](https://htmx.org/attributes/hx-swap/)? Let's say the user edits the name of a cage and `POST`'s a `CageUpdateForm` to the server, which then updates the cage in the database and returns a fresh `cage.html` component in the response, like this:

```python
# partials/views.py
def cage_update(request: HttpRequest) -> HttpResponse:
    {update the cage...}

    template = loader.get_template("partials/cage.html")
    context = {...}
    response = template.render(context, request)

    return HttpResponse(response)
```

First, let's tell the `toasts-container` that it is a `#toasts` element and that it's a target for `out-of-band` swaps.

```htmldjango
<!--toasts-container.html-->
<!-- adds "id" and "hx-swap-oob" -->
<div 
  class="flex flex-col space-y-3 fixed z-30 bottom-4 right-3"
  id="toasts"
  hx-swap-oob="outerHTML"
>
  {% for message in messages %}
    {% include "partials/toast.html" %}
  {% endfor %}
</div>
```
By using `hx-swap-oob` in this way, what we're saying to the `toasts-container` in the response is "if you see your twin element in the DOM, replace them" (that's what the `outerHTML` swap strategy does):

Next, let's create a message (which gets stapled to the session object in the response):

```python
# partials/views.py
def cage_update(request: HttpRequest) -> HttpResponse:
    {update the cage...}

    template = loader.get_template("partials/cage.html")
    context = {...}
    response = template.render(context, request)

    # adds a "message" that will get sent to the client as part of the session
    messages.success(request, message="Cage updated successfully`", extra_tags="Cage updated")

    return HttpResponse(response)
```

Finally, let's append a new `toasts-container` to the response:

```python
# partials/views.py
def cage_update(request: HttpRequest) -> HttpResponse:
    {update the cage...}

    cageTemplate = loader.get_template("partials/cage.html")
    cageContext = {...}
    cageResponse = template.render(cageContext, request)

    messages.success(request, message="Cage updated successfully`", extra_tags="Cage updated")

    # generates a fresh toasts container
    toastsTemplate = loader.get_template("toasts-container.html")
    toastsContext = {...}
    toastsResponse = template.render(toastsContext, request)

    return HttpResponse(cageResponse + toastsResponse) # just add the two responses together!
```

And voila!

<img title = "Toast Example" alt = "toast example" src = "/static/images/hx-redirect/toast-example.gif">

<br/><br/>

For the curious, here's how a `message` is actually consumed in `toast.html`:

```html
<!--toast.html-->
{% load static %}
{% load filters %} 
{% with extra_args=message.extra_tags|split:"; " title=extra_args.0 %}

<div 
  class="..." 
  x-data="{dismissed: false}" 
  x-show="!dismissed" 
  x-init="setTimeout(() => dismissed=true, 8000 * {{ forloop.counter }})"
  x-transition.duration.100ms
>
<!-- INFO -->
{% if message.level == DEFAULT_MESSAGE_LEVELS.INFO %}
  <div class="...">
    <div class="flex flex-row space-x-2">
      <svg class="inline-block align-middle size-7 fill-blue-500">
        <use href="{% static "icons/info.svg" %}#info"></use>
      </svg>
      <div class="flex justify-between w-full">
        <span class="text-md">{{ title }}</span>
        {% include "partials/toast-cancel-button.html" %}
      </div>
    </div>
    <p class="text-xs">{{ message }}</p>
  </div>

<!-- SUCCESS -->
{% elif message.level == DEFAULT_MESSAGE_LEVELS.SUCCESS %}
    {...}

<!-- WARNING -->
{% elif message.level == DEFAULT_MESSAGE_LEVELS.WARNING %}
    {...}

<!-- ERROR -->
{% elif message.level == DEFAULT_MESSAGE_LEVELS.ERROR %}
    {...}

{% endif %}
</div>

{% endwith %}
```

We extract `message.level` to determine the toast appearance and use a sprinkling of [Alpine.js](https://alpinejs.dev/directives/show) to dismiss the toast automatically. Messages are cleared automatically after the client processes the request[^message-expiration].

To summarize: 
- For full-page loads, `toasts-container.html` is already included in the response. So you just set a `message` and that's it.

- For partial responses, you set a message and also include the `toasts-container.html` element as part of the response. `toasts-container.html` has a special element: `<div id="toasts" hx-swap-oob="outerHTML">`. That means that if htmx sees an element in a response with an id of `toasts`, it should look for an element in the current DOM with that same ID and fully replace it.

## Issue with this approach

I've found this approach has some reliability issues. When you click the `Back` button to return to a page, and then complete an action that triggers an app notification to appear, the message framework seems to silently fail. I initially thought it may be an htmx targeting issue - remember the twin analogy from earlier? That relies on htmx first locating the twin `#toasts-container` in the DOM. Maybe htmx is not able to locate the element on the page? Perhaps `#toasts` hasn't rendered yet, by the time the network request fires? Some debugging concluded that this isn't a targeting issue - the `#toasts` element is present on the page, waiting for an element to be out-of-band swapped inside.

Furthermore, duplicate messages sometimes appear on the page, even though only one message has been theoretically created on the server...

I suspect this problem is related to the "behavior of parallel requests"[^parallel-requests]. 

> For example, if a client initiates a request that creates a message in one window (or tab) and then another that fetches any uniterated messages in another window, before the first window redirects, the message may appear in the second window instead of the first window where it may be expected.

## Poka-yoke (ポカヨケ)

Rather than debug Django messages, let's ask - do we need Django messages framework at all for in-app notifications, if we are using htmx? htmx 4 introduced the idea of partial response swaps[^hx-partial] with the `hx-partial` template tag, to provide a more declarative and intuitive mechanism to handle out-of-band swaps. I'm not a huge fan of out-of-band-swaps - they require you to add an attribute to an element that may be in a different HTML template, which isn't [locality of behavior principle](https://htmx.org/essays/locality-of-behaviour/)-friendly. I like LoB - it means I can read code and understand it without needing to find and understand unknown amounts of external contextual code as well.

With partial response swaps, you can now directly wrap the element you want to swap with `<hx-partial>`, and specify the behavior on that element itself! I like this approach, because all the nouns and verbs describing the behavior of the toast notification are now right next to each other, making it easier to read the code and understand what is happening.

So back to the question - do we need Django messages anymore? When I initially designed the notifications feature, I was trying to adopt Django's handy "batteries-included" philosophy[^batteries-included] and avoid reinventing the wheel. But Django messages is designed for applications that utilize full-page refreshes (hence the caveat about the behavior of parallel requests earlier). I like htmx precisely because I *don't* need to fully refresh the page to get server interactivity, but the downside is that this creates some awkward use-cases that Django messages isn't designed for.

Our second use-case of partial swaps is a great match for partial response swaps. The first use case, the full-page reload, is a little trickier to implement. So let's drop Django messages and just use htmx partial response swaps to return the toast partial as needed. We'll be brave and figure out how to handle the full-page reload notifications when we get there. With this approach, we get to eliminate one dependency (and one source of bugs and errors).

## Redesign

### Use Case 1 - partial swaps

Let's go out of order and look at partial swaps first, since that's what `hx-partial` was designed for. First, let's remove `hx-swap-oob="outerHTML"` from the `#toasts` element in `toasts-container.html`:

```htmldjango
<!-- toasts-container.html -->
{% load customtags %}
<div class="fixed z-30 bottom-4 right-3 space-y-3">
  <!-- removes hx-swap-oob -->
  <div 
    class="flex flex-col space-y-3"
    id="toasts"
  >
    <!-- let's also pass a new toast_data variable along -->
    {% include "toast.html" with toast_data=toast_data %}
  </div>
</div>
```

We need a new way to tell our toast what to render, since we're no longer using Django messages - that's what `toast_data` is for. Here's an example of how to set and pass it in as a context variable, in an endpoint called `mouse_revive`.

```python
# views.py
def mouse_revive(request: HttpRequest, mouse_id: str) -> HttpResponse:
    mouse = get_object_or_404(Mouse, id=mouse_id)

    {...revive mouse...}

    # The caller of this function decides 
    # where this updated row should go. 
    # Front-end logic stays on the front-end! 
    mouseTemplate = loader.get_template("mouse-row.html")

    mouseContext = {...}
    mouse_response = mouseTemplate.render(mouseContext, request)

    toastData: ToastData = {
        "toast_type": "success",
        "icon": "🐭",
        "title": "Mouse Revived",
        "message": f"{mouse.name} was revived."
    }

    toastTemplate = loader.get_template("toast.html")
    toastResponse = toastTemplate.render(dict(toastData), request)

    return HttpResponse(mouse_response + toastsResponse)
```

In `mouse_revive`, we revive the mouse, re-generate a new `mouse-row.html`, and staple a `toast` to the response! We define `toastData` as a context variable. I gave that piece of code a little pomp-and-circumstance with it's own type, so the pattern is more legible and reusable. And then we just render the response. It's really as simple as adding both responses together and putting them inside an `HttpResponse` object.

htmx knows to listen for `<hx-partial>`'s that show up in responses. Let's rely on that feature to define `toast.html` as a partial, and wrap it in a special `<hx-partial>` element.


```htmldjango
<!-- toast.html -->
<hx-partial hx-target="#toasts" hx-swap="innerHTML">
  <div 
    x-data="{dismissed: false}" 
    x-show="!dismissed" 
    x-init="setTimeout(() => dismissed=true, 8000)"
    x-transition.duration.100ms
  >
    <div>
      <div class="flex flex-row space-x-2">
        <span>{{ icon|default:"icon" }}</span>
        <div class="flex justify-between w-full">
          <span>{{ toast_title }}</span>
          {% include "toast-cancel-button.html" %}
        </div>
      </div>
      <p class="text-xs">{{ toast_message }}</p>
    </div>
  </div>
</hx-partial>
```

In line 1, `hx-partial` is a special element defined in htmx 4 that is processed into `<template hx type="partial">`[^hx-partial-processing]. The attributes `hx-target` and `hx-swap` define where and how to swap in the contents - in this case, our partial says to htmx, "When you see me in a response, swap my contents into the the `innerHTML` of the element whose id is `toasts`. This is exactly what we want, because we love [LoB](https://htmx.org/essays/locality-of-behaviour/)!

### Use Case 2 - full page redirect

In MouseHouse, certain POST requests require a full reload of the page. Here's one example:

```python
@require_POST
def cage_restore(request: HttpRequest, cage_id: str) -> HTTPResponseHXRedirect:
    cage = get_object_or_404(Cage, id=cage_id)

    {...restore cage...}

    return HTTPResponseHXRedirect(reverse("colony_mgmt"))
```

`HTTPResponseHXRedirect` sets the `HX-Redirect` response header, which signals to the client[^hx-redirect] that we want a redirect to occur. There's no chance to append `toast_data` to the context, because the context is set in a different view function. So let's do something special, and attach `toast_data` to the session, since we do have access to that in the request. Let's create a utility function:

```python
from pydantic import TypeAdapter
from .typedefs import ToastData

def append_pending_toast_to_session(request: HttpRequest, toastDataList: list[ToastData]):
    """Use this when you are issuing a page redirect 
    and also want to include a toast notification 
    after the page reloads"""

    TypeAdapter(list[ToastData]).validate_python(toastDataList)
    request.session["pending_toast"] = toastDataList
    request.session.save()
```

Since we're already using types, let's import `TypeAdapter` from `pydantic` and double-check the data being passed in. `validate_python` will raise a `ValidationError` if any element of the `toastDataList` fails to match the `ToastData` type. For my type nerds, here's the shape of `ToastData`:

```python
# typedefs.py
from typing import Literal, TypedDict

type ToastType = Literal["success", "info", "warning", "error"]

class ToastData(TypedDict):
    """Used to pass toast info via session (e.g. during a redirect)"""

    toast_type: ToastType
    icon: str
    title: str
    message: str
```

So now it's time to use the `append_pending_toast_to_session` function. First, let's update the `cage_restore` view definition (which issues a redirect) and append a toast to the session.

```python
@require_POST
def cage_restore(request: HttpRequest, cage_id: str) -> HTTPResponseHXRedirect:
    cage = get_object_or_404(Cage, id=cage_id)

    {...restore cage...}

    toastData: ToastData = {
        "toast_type": "success",
        "icon": "↩️",
        "title": "Cage Restored",
        "message": f"{CageType(cage.cage_type).label} cage '{cage.name}' was re-opened.",
    }

    append_pending_toast_to_session(request=request, toastDataList=[toastData])

    return HTTPResponseHXRedirect(reverse("colony_mgmt"))
```

Next, let's define a custom Django Template Language tag[^dtl-tags], to pop pending toasts from the session:

```python
# templatetags/customtags.py
from pydantic import TypeAdapter, ValidationError

@register.simple_tag(takes_context=True)
def pop_session_toast_list(context):
    request = context.get("request")
    key = "pending_toast"

    if request and hasattr(request, "session") and request.session.has_key(key):
        try:
            pending_toast_list = request.session.pop(key, None)
            TypeAdapter(list[ToastData]).validate_python(pending_toast_list)
            return pending_toast_list
        except ValidationError as ve:
            print("The pending toast list failed validation and was discarded.")

    return None
```

And then update `toasts-container.html` to look for pending toasts and display them when the page intially loads:

```htmldjango
<!--toasts-container.html-->
{% load customtags %}
<div class="fixed z-30 bottom-4 right-3 space-y-3">
  <div 
    class="flex flex-col space-y-3"
    id="toasts"
  >
    <!-- look for pending toasts and consume/display them -->
    {% pop_session_toast_list as toast_list %}
    {% if toast_list %}
      {% for toast_data in toast_list %}
        {% include "partials/toasts.html#toast" with toast_data=toast_data %}
      {% endfor %}
    {% endif %}
  </div>
</div>
```

Great! We now have a way to attach toast notifications during a redirect!

## Conclusion

We explored two ways to configure in-app notifications with Django and htmx. The first method uses Django messages framework with htmx's `out-of-band swap`, and discovered some reliability issues. For the second method, we took advantage of the new `hx-partial` feature in htmx 4, and got some more readable code out of it as well. I'm still not totally  sure why method 1 had buggy behavior (especially when hitting the "Back" button in the browser) - my best guess is that Django messages framework had some sort of compatibility issues with `hx-swap-oob`, and by eliminating it altogether we only had to solve the quirks of `<hx-partial>`, which means we ended up with a more consistent notification system.

[^message-attach]: <https://docs.djangoproject.com/en/6.1/ref/contrib/messages/#adding-a-message>
[^message-expiration]: <https://docs.djangoproject.com/en/6.1/ref/contrib/messages/#expiration-of-messages>
[^parallel-requests]: <https://docs.djangoproject.com/en/6.1/ref/contrib/messages/#behavior-of-parallel-requests>
[^hx-partial]: <https://four.htmx.org/docs/#partials-hx-partial>
[^batteries-included]: <https://docs.python.org/3/tutorial/stdlib.html#tut-batteries-included>
[^hx-partial-processing]: <https://github.com/bigskysoftware/htmx/blob/four/src/htmx.js#L1046>
[^hx-redirect]: <https://htmx.org/headers/hx-redirect/>
[^dtl-tags]: <https://docs.djangoproject.com/en/6.1/howto/custom-template-tags/>
[^session-usage]: https://docs.djangoproject.com/en/6.1/topics/http/sessions/#using-sessions-in-views
