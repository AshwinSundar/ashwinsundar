+++
linkTitle = "Learning Hard Things"
shortTitle = "Learning Hard Things"
title = "Learning Hard Things"
draft = false
genres = ["other"]
date = 2023-06-01
+++

<img src="https://imgs.xkcd.com/comics/machine_learning_2x.png" alt="xkcd-1838" style="width: 400px;"/>

I took a total of one computer science class in my undergraduate degree. It was a CS class geared towards non-CS majors. The class started at 10AM, which was about 2 hours before my brain started functioning effectively. 

In that class, we were [shown many things](https://www.math.ucla.edu/~akrieger/teaching/17f/pic10a/index.html). Variables! Inputs and outputs! Roman numerals! Classes! As a neuroscience major, I hadn't the faintest clue what the point of any of this was. Was programming supposed to be this esoteric, this alien?

Computer science originated as an offshoot of mathematics. In my younger days, I was good at math. "I got this!", I said.

This classed looked nothing like math, nothing like anything I had seen before...

<img src="dali-sleep.JPG" alt="xkcd-1838" style="width: 600px;" title="A vertical, chronically-tired matriculate"/>

I fell asleep a lot in that class. Several times, I experienced some form of [sleep paralysis](https://en.wikipedia.org/wiki/Sleep_paralysis) - unable to move, unable to breathe, my subconscious listened to the lecturer drone on about objects and assignments and operators. 

Ultimately, I woke up and completed the course with some sort of passing grade, along with a deep distaste for anything related to code. I never took another class from the computer science department again. It would be several years before I'd write another line of code.

## Heuristics

What I did not gain from that class was a set of reusable mental models. In computer science and software engineering, one must rely on mental models to represent complex details and abstractions. The phenomena one works with are often a combination of unobservable and non-existent. Bits and bytes can't be physically observed (unless one works with an [ancient system](https://en.wikipedia.org/wiki/Magnetic-core_memory)). Relationships between services are only as strong as the code that defines them, which itself is merely a conglomeration of symbols that are compiled down to bits and bytes. The good software engineer[^good-topgear] MUST rely on abstractions to make any sense of the world.  

With that established, let's explore a few of my reusable mental models.

## Interfaces are like Legos

Legos interact with each other in a very well-defined manner. The circular interlocking portions must be manufactured to a tolerance of [10 micrometers](https://web.archive.org/web/20121209100137/http://cache.lego.com/upload/contentTemplating/AboutUsFactsAndFiguresContent/otherfiles/download98E142631E71927FDD52304C1C0F1685.pdf) so that the bricks lock as expected, but can be removed easily.

In a good software interface (e.g. an API), the parameters passed around can be defined and characterized precisely, perhaps using input validation and strong typing. The designer of an interface should know and handle all the permutations of data in and data out. If a surface-level function can't handle negative values, then the designer must know how the function will respond.

Back to Legos. Despite their extraordinarily tight specifications, in the precisely-defined Lego universe, there is practically nothing that can't be built with Legos. Six 2x4 bricks fit together in [915,103,765 ways](https://web.math.ku.dk/~eilers/lego.html). It is unlikely any particular design decision by the designers enabled this, but it is as if they built a Turing-complete construction language.

Similarly, good interfaces shouldn't unreasonably constrain the user, at least in the universe that the interface designer has created.

Finally, Lego interfaces behave like a "black box". One can attach a Lego to any interface of an existing Lego project without concern for what color the bricks are, how many bricks are connected, or even the types of all the other bricks involved. The interface is all that matters.

Again, one should not need to dive deep into API source code just to figure out how to use an exposed adapter.  

## Testing is an n-dimensional space

When conducting experiments in school, one learns to modify only one independent variable at a time. This is to make it easy to measure its singular effect on the dependent variable. It is possible to test more variables at once. But it is hard to visualize, more time-consuming, and more difficult to plot nicely in a school report.

Using an idea from statistics called [Design of Experiments](https://asq.org/quality-resources/design-of-experiments), one can change two variables at once, creating a 3-dimensional space with a 3-dimensional functions.

What does this have to do with software testing? A program is effectively a transformation of inputs into outputs. It is easier to think about this for an individual function:

```text
fun (a int, b int) -> int { 
    ...stuff... 
}
```

There are a few ways to test this function. The first is think really hard about common inputs, and make sure the outputs are correct. The next level is to figure out all the edge cases and test those as well. At that point, that function would be considered reasonably well-tested.
But why is that? Why doesn't 100% test coverage mean someone tested **every single possible input**?

Because the style of testing has produced a series of points of data through which a 2d curve can be traced through the 3d test space. The input dimensions are a and b, and the output dimension is the result of the function. As a result, one can interpolate any value within that curve and know what the output is.

This example is clearly very simplified, but the concept can be extrapolated to functions with more complicated inputs, as well as entire programs.

## Conclusion

The vast majority of programming involves taking things on faith. The first level of faith many programmers encounter is faith in documentation - that the vendor of a software accurately describes the details of their abstraction. This is also the first place many programmers' trust is broken. At this point, one must make a decision - dive into the abstraction layer, or abandon the tool and find a different one whose documentation lies less?

Many times, we are forced to choose the former - dive into the details.  This is when it pays to have useful mental models, for the deluge of information is about to become monumental. The HTML core spec is 

```bash
> curl -s https://html.spec.whatwg.org/ | sed 's/<[^>]*>//g' | wc -w
> 571215
```

...that many words long. For a markup language! Fortunately, most HTML tutorials don't just say "read the spec", but involve heavy use of mental models and abstractions. Those models and abstractions are usually right. Usually.

![Pre-mystical-corpuscular](dali-temptation-st-anthony.JPG)

A good heuristic model is similar to a template for a software project. It represents a solid starting point, is applicable for most projects, and can be easily modified or extended. Developing and utilizing these mental models reduces cognitive load and eases the acquisition of new skills.

At the same time, one must avoid peering too closely at the abstraction, for the spindly legs upon which it is mounted may disintegrate and all that's left is dust. 


[^good-topgear]: [JC is the good doctor](https://youtu.be/KmAY4FQ5L4E?si=s4xcaj64S4Xf5eKi&t=155)
