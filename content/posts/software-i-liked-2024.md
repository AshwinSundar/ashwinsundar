+++
linkTitle = 'Software I Liked 2024'
title = 'Long Title'
shortTitle = 'Software I Liked 2024'
date = 2024-11-10T01:02:53-07:00
genres = ['technical']
draft = false
audioFile = "file.mp3"
audioTitle = ""
+++

Here are some new software programs I started using in 2024, and have enjoyed so far:

## keybr.com

In January, I purchased a ZSA Moonlander, which is an ergonomic keyboard with an ortholinear layout. What I did not realize was that I would need to relearn how to type on this setup. After 20+ years of bad habits and pecking at membrane keyboards, I now needed to start back at square one. This shake-up was precipitated by wrist pain from typing constantly. There wasn't a way for me to type less, because of my job, so this required drastic changes. I found keybr and re-learned how to type for the first time since learning from Mavis Beacon in the 1990s as an elementary school student. I went from needing frequent breaks due to hand pain, to being able to type for hours with no pain whatsoever. I still take breaks, but not due to wrist pain anymore.

## NeoVim

In early November, I grew paranoid of my deep dependency on VSCode/Microsoft, and decided to quit cold turkey. I had tried NeoVim in the past, and it was a failure - I was back in VSCode after being frustrated by the Lua configurations. This time around, I employed more patience. I installed LunarVim, which includes a bunch of useful extensions that vanilla NeoVim lacks, such as:

- Telescope, a file finder comparable to the "Go to File" shortcut mapped to `ctrl+p`
- TreeSitter, an incremental parsing library for syntax analysis
- LSP, a language server protocol implementation
- and `lazy.nvim`, a plugin ecosystem manager

I came into NeoVim with a solid theoretical and practical knowledge of Vim, which I lacked the first time around. This has helped greatly, allowing me to guess my way through a number of commands. I've grown to enjoy the "program your editor" aspect of NeoVim, and even enjoy the by-product of learning Lua along the way. I am also greatly enjoyed the massive reduction in RAM usage on my machine. My switch to NeoVim may even let me squeeze more time out of my Mac Mini M1 with 8GB RAM, even though the new M4 is a very tempting offering by Apple.

## Ranger

Ranger is a TUI-based file explorer, which crucially re-maps various Vim keybindings to related actions. For example, `cw` stands for "change-word" in Vim. In Ranger, this lets you rename a file. `dd` in Vim deletes a line, and in Ranger this "delete-yanks" a file, so that it can be moved and pasted elsewhere (via `p`). The original motivation for using this tool was to allow me to keep the slow, ugly File Explorer in VSCode closed at all times, increasing the screen real estate available to actual files. With the switch to NeoVim and use of Telescope, however, my use of Ranger has declined significantly. Still a great tool for direct file actions.

~more to come!~
