+++
linkTitle = "Programming Languages"
shortTitle = "Programming Languages"
title = "Programming Languages"
draft = false
genres = ["technical"]
date = 2022-10-01
+++

I recently began a Coursera course called "Programming Languages", offered by Dan Grossman at the University of Washington. I decided to take this course because the description advertises it as a way to understand the underpinning of all programming languages more thoroughly. When I first learned to program on my own, I always assumed that once I had more experience and learned more languages, I would began to understand the commonalities and differences between programming languages, and that would be sufficient. However, I am realizing that while I do have more experience now, I still lack the big picture view that I desire. Learning Rust made me realize that there is a LOT more to the theory of programming languages than I ever imagined.

I always saw a language as a means to an end - it was merely a tool for creating a program that does something. But a programming language, much like human language, has its own intrinsic meaning, independent of any semantics that are assigned when used in the confines of a particular application.

When I learned programming on my own, I encountered a dizzying number of schools of thoughts on how code should be written, how programs should be modularized, and even what languages should be used. I dismissed a lot of this as pedagogical and irrelevant to my real-world needs of operating a microcontroller or creating a web interface. Why does it matter what C++ is good at, when all that is available to me at work is Javascript?

In retrospect, my view was justified, but myopic. My definition of utility for the first several years of my career was whether I could use it for my job or a side-project I was interested in. But as I've started in my new role in consulting, I'm finding myself switching between projects in completely different industries every 6 months to a year, which is giving me a chance to work in totally different code-bases and languages. Furthermore, I am exposed (via my colleagues on other projects) to far more languages and schools of thought than I was previously.

This has resulted in me becoming particularly interested in the theory of computer science at large, and not just in terms of what is immediately useful to me. I recognize that I have NO IDEA what I'll be working on in 6 months, and as a result everything in CS is potentially useful. This has made the entire field very interesting to me. I get excited by the potential that something I learn now could be useful in the near future. Or it might not be. In which case I can write an article about it.

So anyway, back to the point - Programming Languages is tying things together for me. For example, I just watched a lecture on Options, and recalled the days I spent attempting to understand this bizarre `Option` type in Rust that I kept encountering. It bewildered me because I had never seen such a concept, and it just seemed like a pain to keep wrapping and unwrapping data. Why can't I just access it directly?

The reason for this was more subtle than I could appreciate at the time - I merely saw Rust as a tool to learn so that I could access cooler job opportunities. What I am now appreciating with this course is that languages have intrinsic value. The Option type is a better tool for handling code exceptions, where I might have chose to use a switch statement previously. Sure, the flathead screwdriver worked for prying open a panel in my car, but the `Option` tool is more graceful in the way that a plastic pry device. It is purpose-built. It causes less damage to the underlying structure you are working with.

As I continue through this course, I will update this article.

## December 2022

I have completed half of course 1 and feel like I have a better understanding of the course motivation.

Lecture notes: 
There is no such thing as the **best** programming language, just like there is no such thing as the **best** car. Programming languages, like anything else, are designed to optimize some aspects at the expense of others. To extend the analogy, mechanics might focus on certain types of cars, just like programmers might prefer some cars over others. A good mechanic might have a specialty he prefers, but he generally understands how "cars" (not certain makes/models) work. He won't refuse to work on a car because the upholstery is blue (kind of similar to how programmers bicker about syntax, an unessential detail). A good mechanical engineer knows how cars work, how to get the most out of them, and how to design better ones. Similar analogy to a programming language reseasrcher. 

Older cars (languages) sometimes are better because they are simpler and easier to understand. Popularity in and of itself is not evidence of being the "best".  Software development is precise, you don't get to just guess at how semantics work. You'll sound stupid if you say "I feel that conditional expressions might work like this". 

Idioms make you a better programmer - you can infer how any language works if you understand basic constructs deeply. Booleans, conditional expressions are deep eternal truths about logic. It could be called "first principles" in another world - they hold true regardless of the environment. Understanding programming languages at this level won't get you a better job right away, but they lay a great foundation and enable you to better understand the field as a whole. 

## April 2023

After some delay I've completed Part A. Beyond the course syllabus, here is what I've learned so far:  

 - Programming languages are far more than tools. They are applications of computer science theory. They are conduits of ideas from applied mathematics. There is far more to them than meets the eye. A very human element exists to designing a good programming language - it's an exercise that blends engineering and art.  

Starting Part B of the course, the first lesson includes the following statement that I found enlightening: 


*For some reason, HTML is only rarely criticized for being littered with parentheses but it is a common complaint leveled against LISP, Scheme, and Racket. If you stop a programmer on the street and ask him or her about these languages, they may well say something about “all those parentheses.” This is a bizarre obsession: people who use these languages quickly get used to it and find the uniform syntax pleasant. For example, it makes it very easy for the editor to indent your code properly.  
From the standpoint of learning about programming languages and fundamental programming constructs, you should recognize a strong opinion about parentheses (either for or against) as a syntactic prejudice. While everyone is entitled to a personal opinion on syntax, one should not allow it to keep you from learning advanced ideas that Racket does well, like hygienic macros or abstract datatypes in a dynamically typed language or first-class continuations. An analogy would be if a student of European history did not want to learn about the French Revolution because he or she was not attracted to people with french accents. 

Coming into this class, one misconception I hold is that static typed languages are superior to dynamic typed languages. Static typing is for programmers who know what they're doing and can reason about a program sufficiently. Dynamic typing is for programmers who want to get something working quickly, and leave bugs to the client to deal with. I think my understanding of dynamically typed languages is shaky at best as a result. 
