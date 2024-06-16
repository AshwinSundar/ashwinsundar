+++
linkTitle = "Fibonacci Standard ML"
title = "Fibonacci Series in Standard ML"
draft = false
genres = ["technical"]
date = 2022-12-26
+++

## Challenge  

Write a recursive function in SML that accepts one `i: int` argument and returns a list of Fibonacci numbers of length `i`.

## Approach  

Let's approach this problem in 3 stages. First, we'll write a function that generates Fibonacci numbers, without worrying about recursion or number of arguments. From there, we will progressively improve the function until it meets the requirements of the challenge. 

## Attempt 1

```sml
(* c: current, n: next, lst: list of numbers, i: count to generate *)
fun fibonacci_1 (c: int, n: int, lst: int list, i: int) =
	case i of
		1 => lst
	  | _ => fibonacci_1 (n, c+n, n::lst, i-1)
```

This function accepts four arguments - the current number, the next number, a list of numbers, and the quantity of numbers to generated. For example, `fibonacci_1 (1, 1, [1], 8)` generates the first 8 numbers and returns a list `[21, 13, 8, 5, 3, 2, 1, 1]`.

This function is a bit unwieldy to use for a few reasons. First, a list containing the first Fibonacci number `1` must be passed in, which is not very intuitive. Second, the list that is returned is in reverse order.

## Attempt 2

Next, let's change the function so that it only needs to accept one argument. We will accomplish this by recognizing that the only argument that needs to be passed in by the caller is `i`, and the remaining arguments can be handled by a local function using pattern matching.

```sml
fun fibonacci_2 (i: int) =
	let
		fun f (c: int, n: int, lst: int list, i: int) =
			case i of
				1 => lst
	  		| _ => f (n, c+n, n::lst, i-1)
	in
		f (1, 1, [1], i)
	end
```

The result of `fibonacci_2(8)` is once again `[21, 13, 8, 5, 3, 2, 1, 1]`. This function is much easier to use than `fibonacci_1`, since it only requires one argument - the number of values to generate. 

## Attempt 3

Finally, let's return the list in the correct order by reversing it with another local function that uses pattern matching.

```sml
fun fibonacci_3 (i: int) =
	let
		fun f (c: int, n: int, lst: int list, i: int) =
			case i of
				1 => rev lst
	  		| _ => f (n, c+n, n::lst, i-1)

		fun rev (l : int list) =
			case l of
				[] => []
			  | x::xs => rev xs @ [x]
	in
		f (1, 1, [1], i)
	end
```

The result of calling `fibonacci_3(8)` is `[1, 1, 2, 3, 5, 8, 13, 21]`. The function recursively calculates Fibonacci numbers and only needs one argument passed in, which is the quantity of Fibonacci numbers to generate. Therefore, we have successfully completed the challenge.

## Summary
Through three phases, we iteratively modified the Fibonacci function and ended up with a recursive solution written in a functional programming style.
