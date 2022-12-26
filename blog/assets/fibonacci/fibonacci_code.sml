(*
fun fibonacci_0 (i: int) =
	let 
		val c : int = 1 (* figuring out what value should go here is not hard to reason about, but choosing whether to set this to 0 or 1 is an easy mistake to make *)
		val n : int = 1
		val t : int = 0; (* temporary variable to hold value of c *)
		val lst : int list = [1, 1]	
	in
		while i <> 0 do (
			t := c
			c := n
			n := t + n
			i := i - 1	
		)
		lst
	end
*) 

(* c: current, n: next, lst: list of numbers, i: count to generate *)
fun fibonacci_1 (c: int, n: int, lst: int list, i: int) =
	case i of
		1 => lst
	  | _ => fibonacci_1 (n, c+n, n::lst, i-1)

fun fibonacci_2 (i: int) =
	let
		fun f (c: int, n: int, lst: int list, i: int) =
			case i of
				1 => lst
	  		| _ => f (n, c+n, n::lst, i-1)
	in
		f (1, 1, [1], i)
	end

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
	

