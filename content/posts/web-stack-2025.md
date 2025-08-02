+++
linkTitle = 'PHAT Stack'
title = 'PHAT Stack'
shortTitle = 'PHAT Stack'
date = 2025-07-27T23:27:59-06:00
genres = ['technical']
draft = true
audioFile = ""
audioTitle = ""
+++

My preferred web development stack in 2025 is Django, HTMX, Alpine.js and Tailwind. More generally, I like any of the Python-based web frameworks I've used so far, so we can replace "Django" with "Python" to create a very satisfying acronym - the PHAT[^slang] stack.

## P

I decided that [Python is the language for me](https://ashwinsundar.com/posts/specializing/). Other reasons to like Python:

1) 

2) 

There are a lot of reasons to also not like Python - second-class (or third-class even) support of types; [ugly dunder methods](https://news.ycombinator.com/item?id=44579717#44580071)[^caveat], the 2 to 3 switch[^switch], *what else...?*

## H

Carson Gross's practical manifestation of the [REST Principle](https://en.wikipedia.org/wiki/REST) has truly made me enjoy web development again. As outlined in the excellent book [Hypermedia Systems](https://hypermedia.systems/extending-html-as-hypermedia/#_htmx_html_extended), there are only a handful of updates that need to be made to HTML to really unleash its power as hypermedia:

1) Any element should be able to make HTTP requests (hx-get, hx-post, hx-put, hx-patch, hx-delete)

2) Any event should be able to trigger an HTTP request (hx-trigger)

3) Any HTTP Action should be available (hx-put, hx-patch, hx-delete)

4) Any place on the page should be replaceable i.e. transclusion (hx-target, hx-swap)

HTMX is a simple, closed-scope JavaScript library that grabs declarative syntax from HTML elements[^htmx-syntax] and translates them into well-defined server-behaviors. `hx-get` issues a `GET` request, `hx-post` issues a `POST`, and so on. `hx-trigger` describes what event from the user agent should initiate the request. Finally, `hx-target` and `hx-swap` describes where the representational response should land on the web page. 

## A

Alpine.js (I don't know enough about Alpine right now...)

## T

Tailwind CSS 
    - declarative syntax
    - standalone CLI = no node junk
    - Not a fan of the direction they're going with UI components...but I don't have to care, because of the standalone binary executable.
        - I am worried they will remove it...

## PHAT STACK

Thus, we arrive at the Python, HTMX, Alpine.js, and Tailwind CSS PHAT Stack. I am working my way through each element of the stack, and would consider myself [Proficient](https://daedtech.com/how-developers-stop-learning-rise-of-the-expert-beginner/#:~:text=call%20%E2%80%9CExpert%20Beginner.%E2%80%9D-,The%20Expert%20Beginner,-When%20you%20consider) in Python, HTMX, and Tailwind. I have mainly used Alpine as a tool, and only sparing me, so I would hesitate to call myself anything more than an Advanced Beginner (but hopefully never an [Expert Beginner](https://daedtech.com/how-developers-stop-learning-rise-of-the-expert-beginner/#:~:text=call%20%E2%80%9CExpert%20Beginner.%E2%80%9D-,The%20Expert%20Beginner,-When%20you%20consider)).


[^snow-crash]: I'm halfway through re-reading Snow Crash as I write this. Hence the overwrought, flowery words.

[^slang]: [Origin](https://www.slangsphere.com/understanding-phat-the-evolution-of-a-slang-term/)

[^caveat]: These are the reasons I've either heard or read about by other people. I'm not saying that they are particularly valid reasons though.

[^switch]: Granted I am a newer Python user and don't have the grizzled beard or tales to tell about "the switch", but from [this chart], it appears that people had 11 years to switch fully to Python 3 (released Dec 2008) from Python 2.7 (end-of-life Jan 2020). I would love to hear a specific story or pain-point that this switch created though, I'm still learning here.

[^htmx-syntax]: You don't have to worry about attribute pollution - HTMX attributes are always prefixed with `hx-`, making them very easy to identify (and `grep` for)
