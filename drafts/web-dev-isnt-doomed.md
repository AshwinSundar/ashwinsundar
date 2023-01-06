# Web Development isn't Doomed
August 2022

INTRODUCTION: 
Earlier this summer, StackOverflow released its annual ranking of most-loved programming languages. 61% of developers proclaimed their love for Javascript through this survey. 

This was shocking to me. Developers have voiced so many criticisms of this language for decades (bunch of funny comments pop up on the screen). In a world of constantly changing technologies, why does Javascript persist through everything, like a cockroach during a nuclear holocaust? How was this language still topping the charts in popularity? Was this love affair for Javascript merely Stockholm Syndrome exhibited by developers who don’t know any better? 

For the uninitiated, Javascript is the programming language of the web. In the early days of the web, pages could only be static and lacked interactivity after the page loaded. Seeking to change this, Netscape hired a programmer named Brendan Eich to develop a scripting language for their product Netscape Navigator. He had only 10 days to create the language, and did it. One day I'll do some research to find out how long some other popular programming languages took to develop, and update this section with that information. But I would hazard a guess that Javascript is in a league of its own. 

But wait, I thought Angular/Ember/Gatsby/Meteor/Mithril/NodeJS/Nuxt/Polymer/React/Vue was taking over? Well these are just different ice cream flavors that compile down to the single language your browser understands - Javascript. You might have a case for WebAssembly, but for now we’re stuck with Javascript and its numerous spawn. 

You might be wondering - why am I the ten millionth person to complain about the horrors of Javascript? Because, as we’ll see later, web development is a very twitchy and ADHD field, full of newcomers and non-engineers who don’t know what they’re talking about, and think Javascript should run everything from their website to their toaster. Rest assured, you're welcome to tune out at any time. I’ll try to keep this fun and light-hearted, and only offend Javascript programmers in the process.

THESIS: 
Web Developers aren't doomed. 

II. Relate to the room
This thesis implies that someone, perhaps myself, thinks they ARE doomed. And these hypothetical people have a point. Low-code applications proliferate across the web these days (get a shitty screenshot from Prismic support), convincing programmers and non-programmers alike that they don't need to understand core concepts about programming in order to be a competent developer. This is tautological, and is a reason nothing seems to make sense in web development these days. 

NPM modules continue to spread across the entire observable universe, infecting every single code-base with pointless code (examples from left-pad, isArray, and isArray consensus) and constantly out-of-date dependencies. For the uninitiated - left-pad is an NPM dependency, or snippet of code, that was re-used across thousands of very large, very corporate projects. Projects they should have known better and practiced appropriate risk management in their applications. After a disagreement rooted in the ownership of open-source code, the author rightfully removed left-pad from the NPM ecosystem, causing thousands (how many dependencies were there on the day it was removed?) of applications to either cease working immediately, or be in imminent danger of doing so. In other words, 11 lines of code broke the internet for a few hours in 2016. To NPM’s credit, changes have been made since then, such as restricting unpublishing of publicly-available code. However, the root cause - excessive trust in SOUP - or Software of Unknown Provenance, remains (good opportunity for a joke or some funny pictures).

Here is an example of very simple code that even the newest programmer should be able to write themselves - determining if something is an array. (https://www.npmjs.com/package/isarray). This function is a grand total of 2 lines of code, and really can be written in one line if condensed a bit more:  
```
var toString = {}.toString;
module.exports = Array.isArray || function (arr) { return toString.call(arr) === '[object Array]'; };
```

On the week I created this presentation, this module had been downloaded over 70 million times, in use across a wide variety of production and non-production projects. The size of the module on GitHub, a public code repository, is 3.43 kB. For reference, when I write these two lines of code and save them to a standalone file, it’s 129 bytes. That’s a reduction in file size of 96%. Granted, the module includes other things such as README.md file that explains how to use the function and some tests to make sure the code works, but for a function so miniscule this amounts to quite a bit of unnecessary overhead. 

[next slide of isArray consensus and its contents]
And yeah - isArray consensus (fill in actual name) works by asking 5 different dependencies whether your input is an array, and picks the mode of the answers. It's like cheating off your neighbor and crowd-sourcing your math homework. isArray consensus was created as a joke, but it illustrates a real problem in web development - over-reliance on pointless dependencies. 

This is just one example of a trend ubiquitous across web-programming. Some may know it as DRY - Don't Repeat Yourself (screenshot of first few paragraphs of wiki). In theory, that means minimizing code redundancy so that you can focus on solving unique problems. In practice, we end up with modules like the ones I showed previously.

I contend that the root cause of this is that, on average, web developers have less formal training than any other type of software engineer out there.

I can sense the hush coming over this room. Perhaps what I just said is offensive, or controversial. It is true, you can learn web development autodidactically - through self-learning. But it's a fact. Stack Overflow's 2022 survey reported that web developers, data scientists, blockchain specialists, and students round out the bottom of the list of years of coding experience type by profession (https://survey.stackoverflow.co/2022/#section-experience-years-of-professional-coding-experience-by-developer-type). Yet a near majority of all software engineers consider themselves to be some sort of web developer (survey.stackoverflow.co/2022/#section-experience-years-of-professional-coding-experience-by-developer-type).

This one might be a stretch, but maybe programming communities exhibit their own version of [imprint theory](https://en.wikipedia.org/wiki/Imprinting_(organizational_theory), where the environment that the language was born in influences the community that uses it well beyond its early days. Javascript was born into haphazard programming and deception. Rust was born into a desire to be a better C++, so they always have a chip on their shoulder. I find the history of anything to be so fascinating for this reason, because it helps me understand any topic I'm learning about with far more clarity than I might if I just focus on the here and now.

-----

It's not all doomed though. That was the thesis of this talk after all. So what solutions do I have?

1. Embrace intellectualism. 
Actively seek out quality sources of information. (provide tips on how to do that). It's easy to fall into the trap of miscategorizing quality sources of information. The human brain is tuned to embrace that which is familiar and reject that which is foreign. Only through education and focused effort can we reject this anti-pattern. We can do the same by analyzing sources of information through an objective filter, and only proceeding to consume and assimilate the information if it meets certain criteria of rigor. I recommend everyone decide for themselves what these criteria should be, but here are some guidelines I try to follow for a given piece of information
Is this information written in a way that's appropriate for the content being discussed (less verbose way of saying this?). I don't like calling out particular pieces of content, but there are several very popular web-developer resources that in my opinion are written more childishly than they need to be about a serious concept. This says to me that the information is geared towards beginners in the entire field of computer science, not just beginners in the topic. This is ripe ground for mis-communicating key concepts and establishing a poor foundation for future theoretical knowledge in the subject.
Are adjacent concepts described correctly, with the correct terminology? 
Does the source have a history of writing accurate information that creates correct mental models in the reader's head? This can be more difficult to assess, and requires knowledge of computer science fundamentals in your arsenal. This allows you to quickly perform a litmus test to check if known topics are being discussed correctly.
Is the information placed correctly in the broader ecosystem, or merely described in isolation? This one is a bit unique to my style of learning. I'm a huge fan of the history of any subject. I like to see the relevance of a solution to the broader knowledge base, because that helps me learn and it also helps me assess quickly whether the described solution has the correct "shape" of an answer I'm expecting. 
Of course, these criteria have their own blind-spots as well. So it's important to re-visit your criteria periodically and determine if there are improvements to be made.
Learn the history of computer science. Web development didn't spawn out of thin air with Brendan Eich and Javascript in 1995, or when the internet was invented by Tim Berners-Lee at CERN in 1980, or even when Harvard Mark I was used to crack Enigma in World War II (this point is confusing). Computer science is applied math, and its roots go back hundreds and even thousands of years, for applied math is rooted in logic and philosophy. If this sounds like something you should have learned in some boring history of CS bachelor's degree class, don't despair - I'm in the same boat too, as someone with 0 degrees in computer science. A book I highly recommend to get started backfilling your knowledge of the history of CS is "Ideas that Created the Future" by Harry R Lewis (this should be on the slide the entire time you're talking through this point). In it, Dr Lewis discusses how core ideas in computer science originate with great thinkers starting with Aristotle and progressing through Leibniz, Babbage, and George Boole (pick a better subset of authors once you've read the book further). Once you get into it, the history can be pretty fascinating. (Share a couple of interesting anecdotes?) 
Maybe one more point to nicely round this out? Or make the first two bullet points more detailed

2. Reject anti-intellectualism (what's a better phrase?). This sounds like exactly the same idea as the first point, but is critically important in the modern world. 
Setup: Do you ever feel like you're sifting through a ton of garbage in your search for truth online? This feels like a relatively modern phenomenon for me when I'm searching for answers to my programming questions online. The internet has been a fantastic tool to give a voice to everyone...but not everyone's opinion is valuable, unfortunately. There are a large number of articles written on the internet about computer science by authors that I would consider "Expert Beginners", a concept popularized by a software engineer and author of blog DaedTech Erik Dietrich - (re-read article and kinda type up some paraphrased notes here).
(Screenshot of the ascension up the Expert beginner ladder) This proliferation of garbage content makes it difficult to just auto-didactically learn your way to being an expert in your field. Instead, you run the high risk of becoming an Expert Beginner, where every piece of knowledge you've surrounded yourself with confirms your incorrect view of the world. This risk is ubiquitous in today's social media world, and has leached into the computer science world as well.
Could just show this on a slide while you're talking about another point. "Coding is also permission-less--anyone with an internet connection and some spare time can start coding. As a college dropout, I realized that I could teach myself to code and gain a valuable and rewarding skill. That’s why." - https://twitter.com/ThePrimeagen/status/1529845162524004352 (what's the original quote from? Madison Kanna?)


----

Web developers aren't doomed. They may be at a slight disadvantage compared to the rest of the software engineering community, but there's a way out. It requires focus on the truth, actively seeking quality knowledge, and rejecting poor sources of information. By extension, I hope this talk motivates those of us who write or speak about web programming to up our game a little bit and raise the overall quality of discussion in our community. Thank you. 


