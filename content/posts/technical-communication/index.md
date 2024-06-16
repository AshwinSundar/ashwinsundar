+++
linkTitle = "Technical Communication"
title = "Technical Communication"
draft = false
genres = ["technical"]
date = 2022-08-01
+++

In every technical contributor's career, they will be required to communicate technical work to a non-technical audience. This task typically manifests itself in the form of e-mail, instant message, and one-on-one verbal communication. As they rise through the ranks, they will eventually present their work to larger groups and higher ranks, but the basic lay-person communication task remains the same.

Throughout their career, every technical contributor (TC) will be required to summarized complicated details for a non-technical audience. 
Here are some tips for how to successfully approach these interactions.

## Don't overexplain

Technical employees have to juggle a lot of puzzle pieces in their head at once. A comic by engineer Jason Heeris illustrates this:

![Programmer Interrupted](heeris-2013.png)

The web of complexity that technical employees have to unravel in code that they wrote can be remarkable. And for that reason, when a non-technical colleague or client has questions about what we are working on or why they are experiencing a particular issue, we have a tendency to overexplain everything that we understand in all matters related to and adjacent to the problem.

This can be overwhelming for even your technical colleagues, when they lack the context and expertise that you might have in a corner of the codebase. It's usually better to share a high-level overview of what the problem is and how you're attempting to solve it, and then let your colleague choose the questions they wish to ask (if any). This is more efficient for everyone involved, and it's easier for your colleague to digest the information they need to know. Your colleagues, technical and non-technical, can then explain what you're working on to someone else more clearly, as opposed to saying "I don't really know what they're working on...why don't you go ask Bobitha?".

## Don't patronize

On the other extreme, you don't need to patronize your audience by dumbing down what you're doing. Explaining that Javascript is full of magic fairies that like to randomly zap variables and change how they behave is a crappy way of explaining that Javascript is a weakly-typed language and you don't fully understand implicit coercions yet. One thing I like to do when explaining a subject to someone who isn't familiar is to compare and contrast multiple examples:

 _Javascript is weakly-typed, which means that the language has certain pre-defined assumptions that don't always behave the way you expect, whereas C is more strongly typed and can behave more predictably in the same situations. Finally, all languages exist on a spectrum of weak-to-strong typing, with various advantages and disadvantages on both sides of the spectrum._

There! You successfully communicated a complex topic to a non-technical audience in a way that they can digest and regurgitate as needed.

## Do be in control of the conversation

   When you're deep in a project, you often have an internal map of the trajectories that a project can take. Knowns and unknowns both reside in this map, and it's the unknowns that can land you in trouble. It's helpful to take a probabilistic approach to assessing uncertain situations. For example, on a recent project, I discovered an issue with an interface between two software systems made by two different vendors. When I contacted both vendors for a solution, they each pointed the finger at the other. Rather than communicate this confusing and frustrating turn of events directly to the client, I assessed the situation and determined that either one of two outcomes was likely:

1. Vendor A was responsible for the issue and therefore, for coming up with a solution

2. Vendor B was responsible for the issue and therefore, for coming up with a solution

   I needed to provide an update today, and didn't have time for further research to determine which vendor was responsible. Instead, I recognized that vendor B had been responsible historically for several other bugs in our project. I communicated that due to our past experience, we believed Vendor B was responsible for the issue our client was currently facing. While I need to do more research to determine the root cause, we would follow up with the vendor shortly.

That's a nice, succinct communication to our non-technical client! They were unlikely to care about the nuances of request payloads and how I _think_ Vendor B was producing an incorrect payload that Vendor A was unable to process, but wasn't totally sure yet. For this audience, this explanation would confuse more than illuminate - it would be information overload for them.

----

In conclusion, there is an art to effective non-technical communications. It is a soft skilll that every technical contributor should sharpen for their arsenal arsenal. Every audience is different, so try out each of these tactics, gauge the response of your audience, and tailor your communications appropriately so that you don't have to repeat yourself and you leave your audience happy with the information you provided.

I'll leave you all with this humorous sketch:

https://www.youtube.com/watch?v=BKorP55Aqvg


