+++
linkTitle = 'PHAT Stack'
title = 'PHAT Stack'
shortTitle = 'PHAT Stack'
date = 2026-07-29T11:00:00-06:00
genres = ['technical']
draft = false
audioFile = ""
audioTitle = ""
+++

My preferred web development stack of the last few years has been Django, HTMX, Alpine.js and Tailwind. More generally, I like any of the Python-based web frameworks I've used so far, so we can replace "Django" with "Python" to create a very satisfying acronym - the PHAT[^slang] stack.

## P (ython)

I decided that [Python is the language for me](https://ashwinsundar.com/posts/specializing/).

There are a lot of reasons to also not like Python - second-class (or third-class even) support of types; [ugly dunder methods](https://news.ycombinator.com/item?id=44579717#44580071)[^caveat]; the 2 to 3 switch[^switch]. Programming languages are a [collection of ways to express ideas](https://ashwinsundar.com/posts/programming-languages). Of course, any idea can theoretically be expressed in any Turing-complete language[^turing-complete], but we all know that some languages make certain ideas easier to express than others.

Python makes it easy to express the ideas in my head. It might be a feature/bug of the way I think. I'd rather focus more on building, than techno-psychoanalyzing though.

## H (tmx)

Carson Gross's practical manifestation of the [REST Principle](https://en.wikipedia.org/wiki/REST) has truly made me enjoy web development again. As outlined in the excellent book [Hypermedia Systems](https://hypermedia.systems/extending-html-as-hypermedia/#_htmx_html_extended), there are only a handful of updates that need to be made to HTML to really unleash its power as hypermedia:

1) Any element should be able to make HTTP requests (hx-get, hx-post, hx-put, hx-patch, hx-delete)

2) Any event should be able to trigger an HTTP request (hx-trigger)

3) Any HTTP Action should be available (hx-put, hx-patch, hx-delete)

4) Any place on the page should be replaceable i.e. transclusion (hx-target, hx-swap)

HTMX is a simple, closed-scope JavaScript library that grabs declarative syntax from HTML elements[^htmx-syntax] and translates them into well-defined server-behaviors. `hx-get` issues a `GET` request, `hx-post` issues a `POST`, and so on. `hx-trigger` describes what event from the user agent should initiate the request. Finally, `hx-target` and `hx-swap` describes where the representational response should land on the web page. 

## A (lpine)

Alpine.js is designed for client-side interactivity. What's that? It's when you want your browser to do something without needing to talk to the server. One example of client-side interactivity - clicking a menu button that causes a dialog to appear on the page. You can do this with a little javascript:

```html
<div>
  <button onclick="this.parentElement.querySelector('dialog').showModal()">
    Open
  </button>

  <dialog>
    <p>Hello!</p>
    <form method="dialog">
      <button>Close</button>
    </form>
  </dialog>
</div>
```

Or in Alpine.js:

```html
<div x-data>
  <button @click="$el.parentNode.querySelector('dialog').showModal()">
    Open
  </button>

  <dialog>
    <p>Hello!</p>
    <form method="dialog">
      <button>Close</button>
    </form>
  </dialog>
</div>
```

Here's a more complete example, taken from [MouseHouse](https://mousehouse.bio):

```html
<div class="flex cursor-default w-auto h-auto">
  <button 
    class="cursor-pointer w-auto h-auto {{ button_styles }}" 
    x-data
    @click="$el.parentNode.querySelector('dialog').showModal()"
  >
    {% block dialog_button %}
    {% endblock dialog_button %}
  </button>
  <!-- onclick hides dialog when mousedown ends outside of dialog -->
  <dialog 
    id="{{ dialog_id }}"
    class="fixed m-auto rounded-none border-1 border-black shadow-[5px_10px_1px_0px] {% block shadow_color %}shadow-gray-500{% endblock shadow_color %}"
    x-data="{ flash_dialog_close_button: false }"
    @mousedown="if($event.target === $el) flash_dialog_close_button = true"
    :class="{ 'bg-yellow-50': flash_dialog_close_button }"
  >
    <div class="p-4">
      <div class="flex flex-row justify-between space-x-4">
        <div class="text-2xl font-bold pb-8">
          {% block dialog_title %}
          {% endblock dialog_title %}
        </div>
        {% include "partials/dialog-close-button.html" with close_id=close_id %}
      </div>
      {% block dialog_content %}
      {% endblock dialog_content %}
    </div>
  </dialog>
</div>
```

## T (ailwind)

Tailwind CSS is a declarative way to describe the styles of elements on a web page. This means you can just read the template HTML file and understand how the element will be styled. It will be declared inline, without requiring you to cross-reference CSS stylesheets to figure out what a `container-inner` style is supposed to mean in this context. I especially like that there is a [standalone CLI](https://tailwindcss.com/blog/standalone-cli), meaning I don't need to keep npm around in a Python project.

There was a great talk at Big Sky Dev Conf 2026 (which I attended and will hopefully write about later) about [why you should love Tailwind](https://www.youtube.com/live/edHB5VYjjw8?si=gHcC7P7xVITu5Zwe&t=7991). Anthony's a brilliant engineer with a lot of great ideas, including the sentiment that we can all do more with less. It's a great lesson that the software engineering community could really learn a lot from.

## PHAT STACK

Thus, we arrive at the Python, HTMX, Alpine.js, and Tailwind CSS PHAT Stack. I am working my way through each element of the stack, and would consider myself [Proficient](https://daedtech.com/how-developers-stop-learning-rise-of-the-expert-beginner/#:~:text=call%20%E2%80%9CExpert%20Beginner.%E2%80%9D-,The%20Expert%20Beginner,-When%20you%20consider) in Python, HTMX, and Tailwind. I have mainly used Alpine as a tool, and only sparing me, so I would hesitate to call myself anything more than an Advanced Beginner (but hopefully never an [Expert Beginner](https://daedtech.com/how-developers-stop-learning-rise-of-the-expert-beginner/#:~:text=call%20%E2%80%9CExpert%20Beginner.%E2%80%9D-,The%20Expert%20Beginner,-When%20you%20consider)).


[^snow-crash]: I'm halfway through re-reading Snow Crash as I write this. Hence the overwrought, flowery words.

[^slang]: [Origin](https://www.slangsphere.com/understanding-phat-the-evolution-of-a-slang-term/)

[^caveat]: These are the reasons I've either heard or read about by other people. I'm not saying that they are particularly valid reasons though.

[^switch]: Granted I am a newer Python user and don't have the grizzled beard or tales to tell about "the switch", but from [this chart], it appears that people had 11 years to switch fully to Python 3 (released Dec 2008) from Python 2.7 (end-of-life Jan 2020). I would love to hear a specific story or pain-point that this switch created though, I'm still learning here.

[^htmx-syntax]: You don't have to worry about attribute pollution - HTMX attributes are always prefixed with `hx-`, making them very easy to identify (and `grep` for)

[^turing-complete]: https://en.wikipedia.org/wiki/Turing_completeness#Non-mathematical_usage
