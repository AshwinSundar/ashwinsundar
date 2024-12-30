+++
linkTitle = "Programming Languages"
shortTitle = "Programming Languages"
title = "Programming Languages"
draft = false
genres = ["technical"]
date = 2022-10-01
+++

I recently began a Coursera course called "Programming Languages", offered by Dan Grossman at the University of Washington. I decided to take this course because the description advertises it as a way to understand the underpinning of all programming languages more thoroughly. When I first learned to program on my own, I always assumed that once I had more experience and learned more languages, I would began to understand the commonalities and differences between programming languages. However, years later, I still lack the big picture view that I desire.

I thought that of a programming language as a means to an end - they are merely tools for creating a program that does something. But a programming language, much like human language, has its own intrinsic meaning, independent of any semantics that are assigned when used in the confines of a particular application.

When I learned programming on my own, I encountered a dizzying number of schools of thoughts on how code should be written, how programs should be modularized, and even what languages should be used for a given type of problem. I dismissed a lot of this as pedagogical drivel, irrelevant to my real-world needs of operating a microcontroller or creating a web interface. Why should I care what C++ is good at, when Javascript is all that's available for me to use in my work environment[^yearbook-sidebar]?

In retrospect, my view was justified, but myopic. My definition of utility was whether I could use it for my job or a side-project. But as I've started in my new role in consulting, I'm finding myself switching between projects in completely different industries every year, which is giving me a chance to work in totally different code-bases and languages. Furthermore, I am exposed (via my colleagues on other projects) to far more languages and schools of thought than before, when I worked in a codebase for a proprietary system in the aging, heavily-regulated medical device industry.

As a result, I have become particularly interested in the theory of computer science beyond what is immediately useful to me. Since I generally have no idea what I'll be working on in 6 months, everything in the field is potentially useful. It's exciting to learn again, because anything could be useful in the future.

To bring it back, the Programming Languages course is tying disparate subjects back into a central theory of programming. For example, I just watched a lecture on Options, and recalled the days I spent decoding the semantics of the bizarre `Option` type in Rust. `Option` bewildered me because I had never seen such a concept, to place the result in a container, like some sort of gift, and hand it back to the client for them to unwrap. It just seemed like a pain to keep wrapping and unwrapping data. Why can't I just access it directly?

The reason for this was more subtle than I could appreciate at the time. The `Option` type is a better tool for handling code exceptions, where I might have used a switch statement previously. A flathead screwdriver is an adequate tool for prying interior panels off my car, but a more elegant tool is the plastic pry device. It is purpose-built. It causes less damage to the underlying structure you are working with. Similar merits are provided by `Option`.

## December 2022

Some more notes from the course:

There is no such thing as the **best** programming language, just like there is no such thing as the **best** car. Programming languages, like anything else, are designed to optimize some aspects at the expense of others. To extend the analogy, mechanics might focus on certain types of cars, just like programmers might prefer some cars over others. A good mechanic might have a specialty he prefers, but he generally understands how "cars" (not certain makes/models) work. He won't refuse to work on a car because the upholstery is blue (kind of similar to how programmers bicker about syntax, an unessential detail). A good mechanical engineer knows how cars work, how to get the most out of them, and how to design better ones. Similar analogy to a programming language reseasrcher. 

Older cars (languages) sometimes are better because they are simpler and easier to understand. Popularity in and of itself is not evidence of being the "best".  Software development is precise, you don't get to just guess at how semantics work. It's imprecise and dull to make a statement like "I feel that conditional expressions might work like this". There's a precise definition for a conditional statement that one should use instead.

To become a better programmer , one needs to understand idioms - you can infer how any language works if you understand the basic constructs deeply. Booleans and conditional expressions are deep eternal truths about logic. They are two of the "first principles" concepts of computer science and programming. Understanding programming languages at this level is essential to forming  a solid foundation.

## April 2023

After some delay I've completed Part A. My main takeaway is is that programming languages are far more than tools. They are applications of computer science theory. They are conduits of ideas from applied mathematics. There is far more to them than meets the eye. A very human element exists to designing a good programming language - it's an exercise that blends engineering and art.  

Starting Part B of the course, the first lesson includes the following statement that I found enlightening: 

>> For some reason, HTML is only rarely criticized for being littered with parentheses but it is a common complaint leveled against LISP, Scheme, and Racket. If you stop a programmer on the street and ask him or her about these languages, they may well say something about “all those parentheses.” This is a bizarre obsession: people who use these languages quickly get used to it and find the uniform syntax pleasant. For example, it makes it very easy for the editor to indent your code properly.

>> From the standpoint of learning about programming languages and fundamental programming constructs, you should recognize a strong opinion about parentheses (either for or against) as a syntactic prejudice. While everyone is entitled to a personal opinion on syntax, one should not allow it to keep you from learning advanced ideas that Racket does well, like hygienic macros or abstract datatypes in a dynamically typed language or first-class continuations. An analogy would be if a student of European history did not want to learn about the French Revolution because he or she was not attracted to people with french accents.

Coming into this class, one misconception I hold is that statically-typed languages are superior to dynamically-typed languages. I currently believe that static typing is for programmers who know what they're doing and can reason about a program sufficiently. Dynamic typing is for programmers who want to get something working quickly, and leave bugs to the client to deal with. I think my understanding of dynamically-typed languages is shaky at best as a result. Hopefully, part B will help dispel this myth I cling to.

[^yearbook-sidebar]: Many programmers refuse to part with their favorite language, insisting it is the correct solution for all problems in programming. In college, I faced a similar situation in an entirely unrelated world. I worked for the yearbook as a photographer, and after a year, I was promoted to photography editor. As my first order of business, I set about trying to convince the editor-in-chief that we should switch all photography to film. In the year 2011. This anachronistic proposition came about after I experienced the magic of Velvia 50, a color-positive film known for its rich saturation and high quality. I put together a (seemingly) bulletproof argument towards the merits of film, and presented my contention. As one may guess, my arguments failed to convince the EIC to invest in a stock of film cameras and Velvia film. Rather than accept defeat, I chose to resign as photography editor, because I was unhappy with compromise. I believed I was being principled, but in retrospect, my stubborn-ness lost me a job I had coveted for years, because it wasn't the perfect job I envisioned. Like many decisions, a choice of programming language also ends up being a compromise. If you want to shoot film, it's probably going to be on your own dime and as a hobby. Similarly, if you want to code in Racket or Standard ML, it's unlikely that you'll ever be paid to do so.
