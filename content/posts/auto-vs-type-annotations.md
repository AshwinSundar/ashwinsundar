+++
linkTitle = "auto vs type inference"
title = "auto vs type inference"
draft = true
genres = ["technical"]
date = 2023-02-01
+++

# auto versus type inference

Note: Rewrite and make this better.


April 2023

**Question:** Do `let` in Typescript and `auto` in C++ behave the same way as Standard MLs optional type annotations? 

`auto x = {expr}` is an example of a "placeholder type" specifier. According to [cppreference.com](https://en.cppreference.com/w/cpp/language/auto), this <i>specifies that the type of the variable that is being declared will be automatically deduced from its initializer.</i>. 

How is the type deduced? Using [template argument deduction](https://en.cppreference.com/w/cpp/language/template_argument_deduction#Other_contexts), which is a fancy concept for describing "solving an equation" in math. In the equation, $x+1=7$, it is easy to deduce that $x=6$. Similarly, in the expression `auto x = 3`, it's easy to deduce that the type of x is `integer`. Type deduction can get much more complicated, the study of which belongs to [type theory](https://en.cppreference.com/w/cpp/language/template_argument_deduction#Other_contexts). 

In a strongly-typed language like Standard ML, one is not required to specify parameter types or return types when defining a function. This seems paradoxical at first. If the language is strongly-typed (meaning variable types are known at compile-time), how can a programmer choose to **not** tell the compiler what types the function accepts and returns? 

Early Fortran, COBOL, and C all required explicit type annotations. Standard ML supported type inference in the 1970s, but was one of few languages to do so. Haskell, Scala, Rust, C++, and Typescript all joined afterwards.  

While type inference took some time to make its way into modern languages, the idea has been around for a long time, going back to logician [J Roger Hindley](https://en.wikipedia.org/wiki/Hindley–Milner_type_system), Turing Award winner [Robin Milner](https://en.wikipedia.org/wiki/Hindley–Milner_type_system), and mathematician [Haskell Curry](https://en.wikipedia.org/wiki/Haskell_Curry).

Standard ML supports type-inference natively. It doesn't even require a difference keyword. Just leave off the type annotation:

`var x` <s>`:int`</s>` = 3`
`fun sum (x `<s>`: int`</s>`, y `<s>`: int`</s>`) `<s>` -> int`</s>` = ...`

Here's another example, borrowed from Dan Grossman's Programming Languages course: 

```
val x = 42
fun f (y,z,w) = if y then z+x else 0
```

`x` is given type `int` because 42 is of type int. For the parameters of `f`, `y` must be type `bool` because it is tested in a conditional statement. `z` is of type int because it is being added to something else that is already known to be type `int`. Finally, `w` can be any type because it is never used in the expression. The type for f is `bool * int * 'a -> int`. 

So yes. using `auto` in C++, using `let` in Typescript, and omitting type annotation in Standard ML all represent the same concept - type inference. 
