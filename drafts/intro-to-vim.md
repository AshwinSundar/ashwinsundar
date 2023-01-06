# TITLE
- Introduction to Vim
- A Handy guide to Vim
- The Software Engineer's Guide to Vim (too dramatic?)

## Introduction
Vim, which stands for "Vi-Improved", is a terminal-based text-editor invented by Dutch computer programmer Bram Moolenaar and released in 1991. As the name suggests, it was designed as a successor to the vi text editor released in 1976. In either case, it seems like many programmers these days end up in Vim by accident, as indicated by this popular meme: 

[How to get out of Vim meme]

However, there is a lot more to learn about this quirky little text-editor other than how to exit it back to the safety of VSCode. Vim is great for staying in the terminal and jumping into a file for a quick edit. Billed as "a programmer's text editor" (cite Vim man page), Vim is also an excellent text-editor in its own right and has a lot of the same capabilities that even modern visual text editors have, such as global find-and-replace and multi-line edits.

## Motivation
The vast majority of developers in 2022 use a professional IDE such as Visual Studio Code or IntelliJ (https://survey.stackoverflow.co/2022/#most-popular-technologies-new-collab-tools). These IDEs offer a lot of capabilities for managing large development projects, such as integrated source control, custom keybindings and settings for different projects, and extensions to increase developer productivity. As an added bonus, modern IDEs don't make you feel like you're hacking into the upside-down in the 1980s in some sort of Stranger Things sequel (Disclaimer: I have only seen a couple of Stranger Things so far, but I imagine that's where things are going).

You might be wondering now, why should I stop using tried-and-tested tools that I'm familiar with? By all means, don't stop using your favorite editor! Editors are just tools after all, using a good editor is not the end-goal of writing code. However, it is helpful to know how to use multiple tools. A keyboard and mouse are the only tools a programmer uses to interact with and create lines of code. Vim places all the commands needed to modify code literally at the programmer's fingertips, perfectly organized into a keyboard layout that has not changed in over 100 years (a bit dramatic). While learning Vim has a steeper learning curve, I believe there is a greater scope for improvement in productivity. The point is, you'll know you're using Vim effectively when you are touch-typing your way through files and rarely reaching for the mouse.  
 
The second reason to learn Vim is that the act of using Vim serializes operations in your head. This point is a bit tough for me to express, so here's the first draft. It organizes the thoughts in your brain into a serializable pattern, one that interplays with modifying singular files very effectively. In my opinion, you develop a closer connection to the code you are editing, and it helps you understand it at some deeper level that I can't fully articulate yet.  

- Point 3 - working in Vim strips out all distractions. There are no extensions to bother you, no font schemes to play around with, no annoying contextual help menus to lead you away from your current code. It's just you and a text file, for good or for bad, that's it. This is a different way of working, and could be soon as worse in some ways - why not have all tools always available to you? I like the unadulterated focus I can achieve for certain tasks, such as for taking notes, writing articles, and testing out short snippets of code. For that final use case, I particularly enjoy the extremely rapid build-test-fix cycles I can accomplish without leaving my keyboard. I also find that my mental map of the codebase is in much sharper focus from having to interact with the raw text files with such focus. 

## Installation
Vim is available out-of-the-box on most Unix-based operating systems, such as Linux and macOS, as well as Windows. Simply type `which vim` on Linux or macOS to locate the program in the user's path. If the result of this expression is "vim not found", then Vim can be installed by following the instructions at https://www.vim.org/download.php. 

## How to enter and exit vim
"How to exit Vim" is a common meme at the moment, so let's cover that since I'm guessing 40% of my readers are here for just that. To discard changes and exit vim, type `:q!` and you're free! But instead of running away from our keyboards and jumping for joy, let's re-enter the file and explore a few other useful commands in what is known as Command Line mode.  

To re-enter the file, type `vim <filename>` in the command line prompt. If a file with that name exists, it will be opened in Vim. Otherwise, a new file will be created with that name in the current working directory. 

To enter Command Line Mode, hit `Esc` to exit the current mode and type `:`. At the bottom of the screen you should see the colon character appear, awaiting a command. Let's make a change to this file, save, and then exit. To do that, type "i" to enter what is called Insert Mode. This mode allows you to modify the contents of the file. Create a new line of text, something like "This is my first line of text.", and then hit `Esc` to exit Insert Mode. Return to Command Line Mode by typing `:`, following by `w` to save the file. Finally, type `:q` to exit back to the command line. 
- enter
- exit
- temporarily place in background and return (ctrl+z, fg)

## Modes
We've seem a couple of modes so far - Command Line Mode and Insert Mode, which are two of many modes available in Vim. For this discussion, we will cover four primary modes of interaction with Vim. These are:

- Normal Mode
- Insert Mode
- Visual Mode
- Command Line Mode

Each of these four modes has different key bindings, enabling advanced manipulation of text and files. The vast majority of time is spent in Insert Mode, where text entry and manipulation occurs, although each of the three other modes have their own use cases (don't like this sentence).

| Mode | How to get there |
|------|------------------|
| Normal | `Esc` |
| Insert | `Esc` + `i` |
| Visual | `Esc` + `ctrl+v` |
| Command Line | `Esc` + `:` | 

Normal Mode is kind of like base camp for Vim, so when things go sideways and it's not clear what mode you're in anymore, just hit `Esc` to get back to a known starting point. 

To put it another way, Vim modes can be thought of as a finite state machine and can only exist in a set of defined modes. (see comment at https://stackoverflow.com/questions/11828270/how-do-i-exit-vim?utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform) - recreate that diagram in the comment about finite state machines

## Navigation
Navigating through a file is accomplished in Normal Mode, which you can enter from any mode by hitting `Esc`
| Command | Description |
|---------|-------------|
| h, j, k, l | Move left, down, up, or right one character/line
| w | Advance to the start of the next **w**ord. A word in Vim is defined as a sequence of alphanumeric characters and underscores, separated by non-alphanumeric characters.
| b | Return **b**ackwards to the start of the previous word. 
| 0 | Return to the very start of the current line
| ^ | Return to the first non-blank character in the current line (Useful for tab-indented lines)
| zz | Centers screen on current cursor location 
| gg | Places cursor at the start of the first line of the file 
| G | Places cursor at the start of the last line of the file

## Modification
It might sound strange, but all of the commands below are entered while in Normal Mode, not Insert Mode. That is because if you are in Insert Mode and type a command such as `dd`, it will just modify the file at the current cursor location to insert the characters dd. 

| Command | Description |
|---------|-------------|
| i | Enter **I**nsert Mode at current cursor location | 
| I | Enter Insert Mode at beginning of current line
| A | Enter Insert mode at end of current line
| dd | **D**eletes current line
| dw | **D**eletes next **w**ord
| db | **D**eletes previous word
| d$ | **D**eletes from current cursor location to end of line
| d^ | **D**eletes from current cursor location to start of line, excluding blank characters (such as tab indents)
| dt<char> | **D**eletes **t**o <char>. For example, `dt.` will delete to the end of the sentence, until a `.` is encountered.
| cw | **C**hanges next word and enters Insert Mode. This is the same as typing `dw` and then entering mode immediately. 
| yy | **Y**anks current line to a temporary buffer (not the clipboard). Yank means the same thing as copy, and comes from the old days of teletype machines which had a "yank" command to send text to a temporary holding buffer, which could be "put" (pasted" to a new location. 
| yw | Copies next word to buffer
| p | **P**astes contents of buffer to current cursor location
| > | Indent a line. Can be used in conjunction with a numeric prefix to indent n lines, e.g. `10>` will indent the next 10 lines. 
| < | Un-indent a line
| u | undo. Unlike many programs, there is no limit to how many times you can use the "undo" command.
| ctrl+r | redo. Keep in mind that this command works only immediately after undoing changes. If you undo several times and then choose to start editing again, the redo history is wiped out. (Does this make sense?). This means that using the same macro cannot be used repeatedly without some intermediary setup steps inbetween each macro call to ensure that the next call does what you want. To avoid this pitfall, ensure that the macro you record is record the ENTIRE repeatable sequence of commands you would use to edit n lines of a file in the same way. (Ugh good sentiment but figure out how to word this better)

## Meta Commands (not sure about that name)
All of these commands take place in Command Line Mode, which you can enter by `Esc`aping to Normal Mode and then typing `:`.

| Command | Description |


## Command Composition 
- the best insight I can provide about vim is that you should think of it as a sequence of english commands you are issuing. Modifier keys versus 
- As we saw earlier, there are certain keys such as `d` and `c` that do nothing on their own, but merely describe an action to do to the next command.  
- add n<cmd> to do the command n times

## Visual Mode
I have not used this mode that much, but if it's like the other modes in Vim, then I expect that there are a lot of really cool hidden features that I have yet to discover. In short, to enter Visual Mode, hit `ctrl+v` while in Normal Mode. The cursor will turn into a highlighting block, which you can move around with the navigation commands we learned earlier. The most immediate use case for visual mode is to highlight a specific block of text and hit `y` to **y**ank, or copy the text to the buffer.

## Macros
Before you learn macros, learn how to use `.` effectively. The `.` command repeats the last series of commands issued.Once you're feeling comfortable with basic Vim keystrokes and begin to feel a want for more, you're ready for the world of macros. Macros are a great tool for saving repeatable sequences of keystrokes to the buffer and using them as desired. They take some practice to get right, so let's look at an example first. Here is some code that we need to refactor:

```
const arr = [
(1, 2)
(2, 3)
( 3, 4 )
( 4, 5 )
( 5, 6 )
( 6, 7 ) 
( 7, 8 )
( 8, 9 ) 
( 9, 10 )
]

```
Each entry needs to be separated by a comma, and each tuple is surrounded by some ugly extra whitespace that needs to be trimmed. Yuck! Let's create a macro to fix this. Just like any programming problem, we need to break down the changes we need to make into a sequence of commands that can be chained together repeatedly. To get started, we need to navigate to line 96 using any of the navigation methods we learned earlier. From there, we are ready to come up with a sequence of commands:  
1) `0` + `l` - go to the beginning of the line and advance past the first paranthesis
2) `x` to delete the whitespace character before the first value in the tuple
3) `$` + `h` to go to the end of the line, and then go backwards two characters to the whitespace character after the second value in the tuple
4) `x` to delete the whitespace character
5) `j` to go to the next line.

It can be hard to get the keystrokes perfect the first time around, so I recommend practicing the correct keystrokes on a line or two first. Once you're ready, you can start recording the macro by hitting `qw` and you should see the phrase "recording @w" in the status line at the bottom of the screen. This indicates that the next sequence of keystrokes will be recorded to the `w` key. This also means you can record multiple macros to different keys.

Once you've finished typing the keystrokes, hit `q` again to stop the recording. To use a macro, type `@+<k>`, where k is the key that the macro command was recorded to. In our above example, `@+w` will replay the macro we recorded at the current cursor location. We can enter `@+w` 8 more times to finish formatting the array, or simply type `8+@+w` to replay the macro 8 times. 

Macros definitely take some getting used to, and I certainly still switch to VS Code or another visual text editor for the times where I need to do some serious refactoring in a hurry. But as you use Vim more, you'll begin to see more opportunities to use macros and I highly encourage you take a little bit of time to practice them so that macros become second-nature over time. 

A common pitfall with macros is not ensuring that they are "chain-able". This means that using the same macro cannot be used repeatedly without some intermediary setup steps inbetween each macro call to ensure that the next call does what you want. To avoid this pitfall, ensure that the macro you record is record the ENTIRE repeatable sequence of commands you would use to edit n lines of a file in the same way. (Ugh good sentiment but figure out how to word this better)

In short, here's how to record and replay a macro:
1) In Normal Mode, type `q<key>` to begin recording a macro to <key>
2) Type `@+<key>` to replay the macros at the current cursor location

## Using macros to do a find-and-replace (improve the section title)

**Example 1**:  
In the following code, there should be an underscore in the function name so that it is `get_substitutions1`. 

```sml
fun get_substitutions1(s : string, sll : string list list) =
	case sll of
		[] => []
	  | head::tail => case all_except_option(s, head) of
							NONE => get_substitutions1(s, tail) 
						  | SOME x => x@get_substitutions1(s, tail)		
```

Let's fix this using a macro.

1) Type  `gg` to place the cursor at the top of the file.
2) Type `qw` to start recording a macro to the `w` key.  
3) Search for all instances of the function by typing `:/getsubstitutions` and hitting Enter.
4) Use the navigation key `l` to move right 3 places to the end of the word "get".
5) Enter Insert mode by hitting `i` and then type the underscore character `_`.
6) Hit `Esc` and then `q` to finish recording the macro
7) Type `shift+@+w` to replay the macro and change the next instance of the function name to the corrected value. Alternatively, typing `<number>+shift+@+w` to replay the macro any number of times, in order to find and replace all instances at once.

**Example 2**
Let's prepend the identifier `t1` to the beginning of all variables declared for this test case:  
```sml
val t1_list = ["one", "two", "three", "four", "five"]
val t1_s1 = "one"
val t1_s2 = "two"
val t1_s3 = "three"
val t1_s4 = "four"
val t1_s5 = "five"

val test1 = all_except_option ("string", ["string"]) = SOME []
val test1_2 = all_except_option (t1_s1, t1_list) = SOME ["two", "three", "four", "five"]
val test1_3 = all_except_option (t1_s2, t1_list) = SOME ["one", "three", "four", "five"]
val test1_4 = all_except_option (t1_s3, t1_list) = SOME ["one", "two", "four", "five"]
val test1_5 = all_except_option (t1_s4, t1_list) = SOME ["one", "two", "three", "five"]
val test1_6 = all_except_option (t1_s5, t1_list) = SOME ["one", "two", "three", "four"]
val test1_7 = all_except_option("A", []) = NONE 
val test1_8 = all_except_option("A", t1_list) = NONE 
```

1) Type `gg` to place the cursor at the top of the file.
2) Type `qe` to start recording a macro to the `e` key.
3) Use a regular expression to locate all instances of the either the "list" or "s\*" variables by typing `:/s*\|list`
4) Enter Insert mode by hitting `i` and then typing `t1_` to indicate that these variables are for use in Test 1.
5) Type `w` to advance forward one word.
6) Hit `Esc` and then `q` to finish recording the macro. 
7) Type `16+shift+@+e` to change the remaining instances of the variables.


| Command | Description |
|---------|-------------|
| :reg	  | View macros stored in register (Cmd Line Mode) |
## Hands on practice
- vimtutor should be available, if not install with ...
- VSCode Extension, so you get even more practice
- Best way to learn is just to dive in - edit your code in Vim, but if you're in a meeting or taking notes for a class, try using Vim then even. You'll be slower at first and it can be frustrating, but over time you will slowly speed up until the commands feel second-nature. 

## Advanced commands  
Here are some more advanced commands. 
| Command | Mode | Description |
|---------|------|-------------|
| ctrl + z | Normal | Bring terminal process to foreground and send Vim to background. In terminal, enter `fg` to return to the Vim process
| :%s/text1/text2/gc | Command Line | Global find-and-replace with confirmation for each occurrence | 
| r<char> | Normal | Replace the character after the cursor with <char> |
| "\*yy | Normal | Copies current line to clipboard
| "\*p | Normal | Pastes contents of clipboard to current cursor location
| :term | Command Line | opens a new Terminal window in Vim
| :split <filename> | Opens <filename> in a horizontal split screen view
| :vsplit <filename> | Opens <filename> in a vertical split screen view

## Conclusion
- There is a lot to Vim, this is not a comprehensive guide by any means. The goal here is to make you confident and proficient in Vim, enough so that you can learn to fish for yourselves and discover new commands and shortcuts. 

-----

- Find some youtube tutorials again and read the comments. That's where you can get some cool insights
- Am I discussing Vim correctly? Am I afraid of coming off as naive? Increase the article quality for sure, but also ensure it remains accessible. This article is great -> https://pithological.com/vim-modal-editing/
- I wonder if it's worth grabbing the Practical Vim book and skimming the intro/motivation, and then quickly reading the rest. let's do it
- this could be a hands-on lunch-and-learn, could be fun - don't want to come off as a show-off though, so spend at least the first 5 minutes motivating why it's helpful to be proficient in Vim
