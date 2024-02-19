# Parallel Processing in Rust

Date: April 6th, 2022

[Rust](https://www.rust-lang.org/) is a systems programming language that is quickly gaining traction at well-known companies including Amazon, Discord, Dropbox, Meta, Alphabet, and Microsoft. It is built for [performance, reliability, and productivity](https://www.rust-lang.org/) and has been voted the most loved programming language according to Stack Overflow's [Annual Developer Survey](https://insights.stackoverflow.com/survey) since 2016. Some large-scale commercial projects that have been built using Rust include:

- Mozilla's [Servo](https://servo.org/) parallel browser engine
- Discord's [Read States](https://blog.discord.com/why-discord-is-switching-from-go-to-rust-a190bbca2b1f) service
- Polkadot's [Substrate](https://github.com/paritytech/polkadot) blockchain engine
- Figma's [Multiplayer](https://www.figma.com/blog/rust-in-production-at-figma/) service

All of these real-world use cases of Rust utilize and benefit from concurrent and parallel processing, which can be daunting to implement on a good day, and pretty terrifying when implemented [badly](https://en.wikipedia.org/wiki/Therac-25). Rust helps mitigate concurrency hazards by design, but it's still up to the programmer to construct their program logic thoughtfully so they can take advantage of the power of concurrent and parallel processing.

**When should I use concurrent or parallel processing, instead of serial processing?**

Most modern processors have multiple cores to work with, which means you can use these cores to achieve significant performance gains:

- When you have a lot of independent computations to process, such as a giant for-loop.
- When some of your threads contain computations that are particularly lengthy to calculate. It's nice to run these on the "backburner" without blocking your program from performing other computations.
- When you have low [parallel overhead](https://www.mathworks.com/help/parallel-computing/decide-when-to-use-parfor.html)

**How do I implement parallel processing in Rust?**
My favorite way to learn new programming languages is by combining it with my love for math and solving problems in [Project Euler](https://projecteuler.net/). To demonstrate parallelization in Rust, let's solve a [simple problem](https://projecteuler.net/problem=1) that I tweaked slightly so we can focus on the implementation of our solution:

_If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1,000,000._

**Solution Methodology**
While the mathematically elegant solution would be to use an [arithmetic series](https://en.wikipedia.org/wiki/Arithmetic_progression), let's just focus on the simple solution, which is to figure out if each number in the range is divisible by 3 or 5. If it is, let's add it to a running sum we're keeping track of.

**Example 1 - No parallelization**

```rust
fn euler1_unpar(input: i32) -> i64 {
    let mut sum: i64 = 0;
    for i in 1..input {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i as i64;
        }
    }
    sum
}
```

**Code walkthrough:** In this example, we accept an `input`, and iterate on every number between `1..input` to determine if it is divisible by 3 or 5 using the modulo `%` operator. If it is, then add the value to a running `sum` we're keeping track of. At the end, return the sum. In Rust, you can return a value by simply calling it without a semicolon after the expression. Since Rust is a [strongly-typed](https://en.wikipedia.org/wiki/Strong_and_weak_typing) language, we need to tell the compiler to add the original `i32` input and convert the sum to an `i64`, so that we have enough space to store the answer.

Let's calculate a performance benchmark for this function so we can compare it to our multithreaded optimization that we'll write next. We can calculate this benchmark with the [easybench](https://docs.rs/easybench/latest/easybench/) crate, an importable package in Rust.

```rust
use easybench::{bench};
let input = 1000000;
println!("euler1_unpar: {}", bench(|| euler1_unpar(input) ) );

>> euler1_unpar: 14.429298ms (R²=0.999, 70 iterations in 21 samples)
```

Our unparallelized function takes about `14.4` milliseconds to execute.

**Example 2 - Parallelized (2 threads)**

```rust
fn euler1_par(input: i32) -> i64 {
    use std::thread;

    let handle1 = thread::spawn(move || {
        let mut thread1_sum: i64 = 0;
        for i in 1..input / 2 {
            if i % 3 == 0 || i % 5 == 0 {
                thread1_sum += i as i64;
            }
        }

        thread1_sum
    });

    let handle2 = thread::spawn(move || {
        let mut thread2_sum: i64 = 0;

        for i in (input / 2)..input {
            if i % 3 == 0 || i % 5 == 0 {
                thread2_sum += i as i64;
            }
        }

        thread2_sum
    });

    handle1.join().unwrap() + handle2.join().unwrap()
}
```

**Code walkthrough:** Here, we use the `thread` module so that we can take advantage of the native multithreading available in Rust. A new thread is created by calling `thread::spawn`, into which a `closure` is passed. [Closures](https://doc.rust-lang.org/book/ch13-01-closures.html) are anonymous functions that allow you to access environment variables, such as the `input` variable. This closure does the same mathematical computation as `euler1_unpar`, except we only process one half of the total range in the thread. The other half is saved for the second thread. We also need to `move` a copy of the input into the closure's scope so that the thread can take ownership of the data and use it. Writing code like this can seem tedious and time-consuming, but is required by Rust to help reduce the risk of [concurrency errors](https://doc.rust-lang.org/book/ch16-00-concurrency.html).

`thread::spawn` returns a `JoinHandle` type, which contains some convenience methods that allow us to take back control over the threads and handle their results. In this case, `JoinHandle::join()` halts execution of the function until our threads have finished their calculations. `.unwrap()` exposes the answers we've calculated in each thread, and then finally we sum those answers up.

Let's see how long this function takes to run:

```
use easybench::{bench};
let input = 1000000;
println!("{}", euler1_par(input));

> euler1_par:  7.345441ms (R²=0.998, 133 iterations in 27 samples)
```

The parallelized function takes about `7.3` milliseconds to execute.

**Conclusion**
The parallelized code runs almost twice as fast as our unparallelized code, and we seem to only lose a little performance due to the overhead of setting up the threads. Nice!

This example demonstrates a way to get started with parallel processing in Rust. You often need to design your program with parallelization in mind from the get-go, as you are forced to think about the flow of your code and determine what pieces of the code take the longest to run and would benefit from parallelization.

_This article was originally written for the [engineering blog](https://engineering.deptagency.com/parallel-processing-in-rust) at DEPT®, a technology consultancy_
