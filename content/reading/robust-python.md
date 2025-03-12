+++
linkTitle = 'Patrick Viafore - Robust Python (2021)'
title = 'Robust Python - Write Clean and Maintainable Code'
shortTitle = 'Patrick Viafore - Robust Python (2021)'
date = 2025-03-09T13:16:32-06:00
genres = ["reading", "2024"]
draft = false
+++

*note to self - move this to 2025 reading*

## Chapter 1 - Introduction to Robust Python

*Clean code expresses its intent clearly and concisely, in that otder. When you look at a line of code and say to yourself, "ah, that makes complete sense," that's an indicator of clean code.* (p 3) 

*There are often specific practices tied to writing clean code, including:*
- *Organizing your code in an appropriately granular fashion*
- *Providing good documentation*
- *Naming your variables/functions/types well*
- *Keeping functions short and simple* (p 3)

*The first step to making code that lasts is being able to communicate through your code.* (p 5)

**Law of Least Surprise**: *When someone reads through the codebase, they should almost never be surprised at behavior or implementation (and when they are surprised, there should be a great cmoment near the code to explain why it is that way)...a program should always repsond to the use in the way that astonishes them the least. Surprising behavior leads to confusion. Confusion leads to misplaced assumptions. Misplaced assumptions lead to bugs. And that is how you get unreliable software.* (p 17)


## Chapter 2 - Introduction to Python Types

*Types convey information. They provide a representation that users and computers can reason about...* (p 23)

**Mechanical Representation**: *Types communicate behaviors and constraints to the Python language itself.* (p 23)

**Semantic Representation**: *Types communicate behaviors and constraints to other developers.* (p 23)


### Typing Systems 

**Strong Versus Weak**: Strongly-typed languages have a **strong** coupling between the semantic and mechanical representation of types. For example, in a strongly-typed language, if a programmer breaks a contract semantically, the compiler will stop and not attempt to infer any types - it will force the programmer to fix the mistake before continuing. Conversely, a weakly-typed language will attempt to infer the type and intended operations so that it can continue execution. Both types of languages have pros and cons. 

*Python falls toward to strong side of the spectrum. There are very few implicit conversion that happen between types.* (p 29)

**Dynamic Versus Static**: In a statically-typed language, one must define the the type information for a statement or expression explicitly - i.e., they must state the semantic representation. By contrast, dynamically-typed languages resolve the type information from the value or variable itself. e.g. `i=1`, `i` is inferred as an integer in a dynamically-typed language. In a statically-typed language, one is required to write `int i = 1`

*Python is a dynamically-typed language...Python has no qualms about changing the type of a variable at runtime.* (p 30)

**Duck Typing**: *The ability to use objects and entities in a programming language as long as they adhere to some interface.* (p 31) 

*If it walks like a duck and quacks like a duck, and you are looking for things that walk and quack like ducks, then you can treat (the object) as if it were a duck.* (p 32)

## Chapter 3 - Type Annotations

*Type annotations are for type-hinting; you are providing notes for the future to improve communication. You don't need to state the obvious everywhere.* (p 39) 

*Typecheckers catch a specific class of errors: those of incompatible types." (p 43)


