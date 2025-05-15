+++
linkTitle = 'Language Specialization'
title = 'Language Specialization'
shortTitle = 'Language Specialization'
date = 2025-05-15T00:28:26-06:00
genres = ['technical']
draft = false
audioFile = ""
audioTitle = ""
+++

I began programming professionally in 2016, and after about 8 years and change, I finally feel ready to pick a language to specialize in. 
I've decided that **Python** is that language. Here is why.

## Intuition

Something about the language clicks with me. 
While I'm not a huge fan of [magic methods](https://en.wikipedia.org/wiki/Method_(computer_programming)#Special_methods), the majority of these methods (a.k.a. *dunder methods*, short for *double-underscore methods*) in Python feel sensibly-named to me. 
That's not to say they are the *most*-sensible names for what they accomplish - but I feel like they provide enough info to hint at what they accomplish, without being overly verbose.

| Magic method | Used for |
| - | - |
| `__add__`, `__sub__`, `__mul__`, `__div__` | Arithmetic operations |
| `__bool__` | Implicitly converting to Boolean for `if <expression>` checks |
| `__and__`, `__or__` | Logical operations |
| `__getattr__`, `__setattr__`, `__delattr__` | Attribute access | 
| `__le__`, `__lt__`, `__eq__`, `__ne__`, `__gt__`, `__ge__` | Comparators |
| `__str__`, `__repr__` | Convert to `string` or another `representational` format |

*Adapted from <u>Robust Python: Write Clean and Maintainable Code</u> by Patrick Viafore, page 166*

One could guess-understand most of these methods and what they do, without reading any further documentation.
That's definitely a pro in my book.

Python's embrace of duck-typing also makes a lot of sense to me. 
Duck-typing, which I think should be called "interface-matching" instead, allows one to "match" a type by dictating which behaviors it is supposed to implement.

Let's say you have two objects, `Dog` and `UnknownAnimal`. 
One could state that `Dog`s can `bark`, `sit`, and `eat`. 
If `UnknownAnimal` can also do those three things, then one can infer that it is probably a `Dog`.
If this doesn't sound like enough info to categorize an `UnknownAnimal` as a `Dog`, then add more things that `Dog`s do - `walk`, `fetch`, `be_a_good_boy` - whatever is needed to narrow down the interface.

I find this wonderfully logical and a practical application of [Set Theory](https://en.wikipedia.org/wiki/Set_theory).

## Flow State

In the past few years, I've started studying computer science in earnest, as opposed to being a dabbler in languages as tools. 
It's an endlessly fascinating field, with interesting connections to every other field in science, engineering, and even the [liberal arts](https://en.wikipedia.org/wiki/Chomsky_hierarchy).

But ultimately, I'm interested in making things which other people can do cool stuff with.
To do that effectively, I want to be able to focus on the problem domain, not the language domain. 
Python does a nice job of getting out of the way and letting me solve a problem.

I recently learned about [Model Context Protocol](https://modelcontextprotocol.io/introduction), an Anthropic API for interfacing LLMs with arbitrary code. 
It is incredibly powerful, as some attendees and I at a [recent tech forum](https://www.wintertechforum.com/) discovered.
We were able to create a terminal-based LLM UI that could be used to interrogate various endpoints and summarize information.
The demo our small team came up with was extremely compelling, and allowed us to rapidly validate an idea in less than 1 day.

This ability to rapidly prototype is a very important feature to me - I want to figure out if an idea is worth pursuing, without having to stand up a bunch of boilerplate code and establish so-called "software best-practices". 

I like the progressive-enhancement feature of Python - one can progressively add robustness to Python code by adding optional type hints and structure to the code, without disrupting the underlying functionality. 

Python enables a really nice "flow state" - I can code without worrying too much about the underlying language mechanics, until I want to.

A big issue historically in Python development has been the lack of a good package management solution. 
`pip` and `venv` can be challenging to work with and debug.
However, I recently learned about [`uv`](https://github.com/astral-sh/uv), which replaces several disaparate tools, adds a lockfile, handle Python version management, and is universally available. 
This is yet another step forward in making Python a great option for getting into a solid flow state while coding.  

## It's where the cool kids are playing

Scientists and researchers seem to prefer Python. 
An unintentional mistake I made in grad school was to complete my master's work in MATLAB and R, thinking those were beneficial for my career prospects. I had heard engineers tend to use MATLAB for calculations, so it only made sense to demonstrate proficiency in it by writing a novel algorithm in it.
Python barely registered in my mind in 2016 as a language to write a signal-processing algorithm. 
Jupyter Notebook was new, but seemed incomplete compared to MATLAB's integrated programming and problem-solving environment. 
So I chose the latter as the language to implement an empirical mode decomposition algorithm, for processing a non-linear signal in the form of an electrocardiogram.

I've considered re-writing my master's project and potentially turning it into a library for handling ECG data with a non frequency-domain technique, which can be useful in low-power applications.
I had no idea how to do this in MATLAB (and still have no idea). 
But Python could be a promising alternative. 

## Conclusion

My next steps are to go all-in on Python. I learn best with books and text, so I've picked up "Robust Python" by Patrick Viafore, along with the massive tome "Fluent Python" by Luciano Ramalho. I hope to get through large sections of both books in the next year and advance my knowledge of Python. I look forward to this journey!
