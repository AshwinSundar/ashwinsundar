+++
title = "Replacing Django Messaging Framework with hx-partial swaps"
date = 2026-09-08
genres = ["technical"]
draft = true
+++

TODO:
[x] use case 1
[] use case 2
[] use case 3
[] proofread
[] post

AUDIENCE: Myself - experienced htmx user, trying to figure out how to solve a bug and refactor toasts into a simpler implementation.

MouseHouse implements in-app notifications using the Django messaging framework and an htmx v2 out-of-band swap.

## Original Implementation

1) A `toasts.html` template lives on the `common.html` template that all pages in the site use.

### `common.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    {...}
</head>
<body>
  {% block body %}
  {% endblock body %}
  <div class="fixed z-30 bottom-4 right-3 space-y-3">
    {% include "partials/toasts.html" %}
  </div>
</body>
</html>
```

### `toasts.html`
```html
  <div 
    class="flex flex-col space-y-3"
    id="toasts"
    hx-swap-oob="afterend"
  >
    {% for message in messages %}
      {% include "partials/toast.html" %}
    {% endfor %}
  </div>
```

- Notice the `hx-swap-oob="afterend"` declaration. This says that if any response which originated from an htmx request[^htmx-header] includes an element with this id (`#toasts`) in it, take that element and swap it in here `afterend` - at the end of the inner content. The existing loop is to handle any messages that were already present on the backend but not shown to the user yet. 

### toast.html

```html
{% load static %}
{% load filters %} 
{% with extra_args=message.extra_tags|split:"; " %}
{% with title=extra_args.0 %}

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
{% endwith %}
```

2) To trigger a toast notification, create a new `message` and pass the `toasts.html` template as part of the response, like this:

```python
def litter_create(request: HttpRequest) -> HttpResponse:
    try:
        {...create a litter}
        messages.success(
            request,
            message=f"A new litter was created.",
            extra_tags="New Litter",
        )
    except Exception:
        messages.error(
            request,
            message="Could not create this litter.",
            extra_tags="Error",
        )

    cageTemplate = loader.get_template("partials/cage.html")
    cageContext = {...}
    cageResponse = cageTemplate.render(cageContext, request)

    toastsTemplate = loader.get_template("partials/toasts.html")
    toastsResponse = toastsTemplate.render({}, request)

    return HttpResponse(cageResponse + toastsResponse) # just add the responses together!
```

Remember how `toasts.html` had a `<div id="toasts" hx-swap-oob="afterend">` element? That means that if a response comes through and contains an element with that same id, it should be swapped `afterend`.

For full page loads, you don't even need to pass the toastsTemplate - `toasts.html` is already included in the `common.html` template that every page uses. Just set a message and return the page.

```python
def index(request: HttpRequest) -> HttpResponse:
    messages.success(request, "Welcome to MouseHouse!", extra_tags="Welcome!")

    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))
```

Messages are cleared when the response is processed by the client[^msg-processing].

<img title = "Toast Example" alt = "toast example" src = "/static/images/hx-redirect/toast-example.gif">

Easy! Sort of.

## Issue with this approach

This approach has some reliability issues that I haven't been able to pinpoint until recently. When you click the `Back` button to return to a page, and then complete an action that triggers an app notification to appear, it just silently fails. It's not a targeting issue - the `#toasts` element is present on the page, waiting for an element to be out-of-band swapped inside. It's the Django messaging framework which is silently failing...

Furthermore, duplicate messages sometimes appear on the page, even though only one message has been theoretically created on the server...

I suspect this problem is related to the "behavior of parallel requests"[^parallel-requests]. 

> For example, if a client initiates a request that creates a message in one window (or tab) and then another that fetches any uniterated messages in another window, before the first window redirects, the message may appear in the second window instead of the first window where it may be expected.

## Poka-yoke (ポカヨケ)

Do I need Django messages framework at all? htmx 4 introduced the idea of partial response swaps[^hx-partial], to provide a more declarative and intuitive mechanism to handle out-of-band swaps. I'm not a huge fan of `hx-swap-oob` - it requires you to put a tag on an element that may be in a different HTML template, and the behavior is a little too implicit for my liking. **(could use more clarification)**

With partials, you can now wrap the element you want to swap in directly with `<hx-partial>`, and specify the behavior on that element itself! This reads a lot more intuitively - all the verbs are on the same line, making it easier to read the code and understand what is happening. **(i don't like the phrase "easier to read" - can you be more specific?)**

So back to the question - do I need Django messages anymore? When I initially designed the notifications feature, I was trying to use the "battery-included" philosophy[^batteries-included] and avoid reinventing the wheel. But Django messages is designed for applications that utilize full-page refreshes (hence the caveat about the behavior of full page requests earlier).

I generally don't use full-page refreshes when returning htmx responses - this allows me to return a minimum payload of just the content which has changed. So no, let's drop Django messages and just use htmx to return the toast partial as needed. We eliminate one dependency and potential for bugs and errors with this approach.

## Redesign

### Use Case 1 - partial swaps
The first example of just returning a toast partial is easy to refactor. Let's first rewrite `toasts.html`:

`toasts.html`
```htmldjango
{% load customtags %}
<div class="fixed z-30 bottom-4 right-3 space-y-3">
  <div 
    class="flex flex-col space-y-3"
    id="toasts"
  >
    {% include "toast-generic.html" with toast_data=toast_data %}
  </div>
</div>
```

The Tailwind CSS classes in `toasts.html` fix the notification to the bottom right of the page. The `id=toasts` will be used by our `hx-partial` below to identify which element to target for the swap.

`toast-generic.html`
```htmldjango
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

In line 1, `hx-partial` is a special htmx 4-defined element that is processed into `<template hx type="partial">`[^hx-partial-processing]. The attributes `hx-target` and `hx-swap` define where and how to swap in the contents - in this case, our partial says to htmx 4, "When you see me in a response, swap my contents into the the `innerHTML` of the element whose id is `toasts`. 

The inner div uses `alpine.js` to auto-dismiss the toast after 8 seconds.

Finally, let's look at how to use this toast in a view to trigger a notification. `mouse_revive` does what it says - it revives a sacrificed mouse.

```python
def mouse_revive(request: HttpRequest, mouse_id: str) -> HttpResponse:
    mouse = get_object_or_404(Mouse, id=mouse_id)

    {...revive mouse...}

    # The caller of this function decides where this updated row should go. Front-end logic stays with the front-end code! 
    mouseTemplate = loader.get_template("mouse-row.html")

    mouseContext = {...}
    mouse_response = mouseTemplate.render(mouseContext, request)

    toastData: ToastData = {
        "toast_type": "success",
        "icon": "🐭",
        "title": "Mouse Revived",
        "message": f"{mouse.name} was revived."
    }

    toastsTemplate = loader.get_template("toast-generic.html")
    toastsResponse = toastsTemplate.render(dict(toastData), request)

    return HttpResponse(mouse_response + toastsResponse)
```

In "mouse_revive", we do whatever needs to be done to revive the mouse, generate a new mouse template as the response, and staple a `toast` response as well! That's it. htmx knows to listen for `<hx-partial>`'s that show up in responses, and use the strategy defined in the partial to place the response in the correct spot. No more cross-referencing other templates to figure out where an out-of-band swap may be occurring! **say this a little better?**

### Use Case 2 - full page redirect
The second example was a little more complicated. This is actually the correct use case for Django messages - a full page refresh that already includes the `#toasts` div in the response. What happens if I include the element again? Will it actually get swapped in, even though its part of the same response?

{ does this approach work? how do i make it work? }

### I lied...there's a third use case

So I told a little white lie earlier...I actually do have a few cases where I want to trigger a full page redirect from htmx. Here's an example:

But we can re-use the solution from before here as well! The pattern isn't any different.



[^htmx-header]: htmx attaches a `HX-Request: true` header to the request.
[^msg-processing]: https://docs.djangoproject.com/en/6.1/ref/contrib/messages/#expiration-of-messages
[^parallel-requests]: https://docs.djangoproject.com/en/6.1/ref/contrib/messages/#behavior-of-parallel-requests
[^hx-partial]: https://four.htmx.org/docs/#partials-hx-partial
[^batteries-included]: https://docs.python.org/3/tutorial/stdlib.html#tut-batteries-included
[^hx-partial-processing]: https://github.com/bigskysoftware/htmx/blob/four/src/htmx.js#L1046
