+++
title = 'Diagrams as Code'
date = 2024-02-29T17:24:50-07:00

draft = true
+++

Creating and maintaining documentation tends to be the least favorite part of many engineers' jobs. A major pain point in the process of maintaining documentation is that, while a product is in development, documentation tends to go stale quickly. This can occur for a number of reasons:

- Engineers don't know how to create useful documentation
- Documentation is kept separately from the work being done
- Only a small subset of engineers are tasked with creating and maintaining documentation

The first problem is a large challenge. Learning how to write good documentation is an entire course. Learning how to create good diagrams is an entire course. 

Fortunately, the last two problems can be partially addressed relatively easily - by saving diagrams as code.

## Definitions

- <u>Diagram</u>: A visual representation of an engineered system
- <u>Code</u>: Text that makes a machine do things
- <u>Version Control</u>: A system that tracks atomic changes to a file

Put that all together:

- <u>Diagrams as code</u>: A text file that is parsed to generate an image, and which can be committed to version control.

## Why save diagrams as code?

- Diagrams should not be an artistic exercise
- Diagrams should be version-controlled with reliable tools
- Diagrams should be useful for new team members

## 1. Engineering diagrams aren't a form of artistic expression

Picture this scenario - you construct a perfect symmetrical system diagram, arranging subsystem components in rounded boxes at the vertices of an equilateral pentagon. It is beautiful; it is pristine.

And then someone decides to add a subsystem.

The solution is simple: 

- Care less about whether boxes in a diagram line up
- Care more about what the boxes actually communicate

## 2. Diagrams should be committed to version-control

Many WYSIWYG/visual-first tools have poor "version-control". These tools typically allow a user to "checkpoint" an image manually. But the checkpoints often have cryptic names, such as "v.203". If a mistake is made, there is no way to easily figure out the last "good" state of a diagram.

The solution here is to use a text-based diagramming tool, so one may take advantage of fully-featured version-control systems, such as `git`. Mistakes can be traced with `git bisect`. The commit history can easily be searched from the command line. All of the powerful capabilities of `git` can be used to track changes to a diagram.

## 3. Diagrams should be useful to new team members

Last, and most importantly - diagrams must be useful to new team members. Imagine that a new member joins the team, and needs to understand the architecture of a codebase. Naturally, they will reach for documentation. But they discover that the documentation is out of date.

Stale documentation can be worse than no documentation. New team members cannot distinguish stale from up-to-date documentation, and will develop an incorrect mental model of the system. This can be very difficult to correct once the damage is done.

The solution is to keep documentation as close to code as possible. Ideally, it should live in the same repo as the code. A task for every pull request should be to review relevant documentation and include updates if needed. This extra work to maintain documentation will save hours of time trying to re-explain how a system works, to a team member that has learned the wrong information. 

## How does one actually create a "diagram as code" diagram?

There has recently been a renaissance of "diagram as code" tools. The one with a lot of momentum currently is mermaid.js. Other popular tools include ZenUML and PlantUML. 

But what about tools like LucidChart, diagrams.net, and Microsoft Visio? These are very popular for remote whiteboarding sessions, for example. Why can't the outputs of those tools simply be committed to version control?

| Tool | Can be VC'd in e.g. git | Text -> Image | Addressable in PR | 
| - | - | - | - |
| mermaid.js | Yes | Yes | Yes | 
| ZenUML | Yes | Yes | Yes |
| PlantUML | Yes | Yes | Yes |
| draw\.io/diagrams.net | Yes | No | No |
| LucidChart | Yes | No | No |
| MS Visio | Yes | No | No |
| Cell phone pictures of whiteboards | Yes | No | No |

In the chart above, I have selected the following criteria to compare tools by:

- Artifacts can be version-controlled in e.g. git
- Artifacts are purely text, and are used to construct a diagram
- Artifacts can be atomically addressed in a pull request

In theory, one may commit any file type to version control. In practice, there is limited value to using version-control to track changes to a .jpeg or .svg file type, which in both cases represent an image. Text can be diff'd down to the singular character, while this is not feasible when the file type is an image. An .svg contains too much "cruft", for lack of a better word - that is, non-value-add information that describes what an image looks like, rather than the relevant data contents of the image.

## Examples

Enough pedantry, let's take a look at actual examples. I have taken a liking to a tool called mermaid.js lately, so all of the following examples will use that tool.

### A sequence diagram, built entirely from text

- what is a sequence diagram, in a couple sentences. why might one use it
- mermaid.js example
- make a change, run git diff

### entity-relationship diagram

- very useful, typically used for db diagrams, can be used for describing relations between any set of subsystems

## Conclusion

Prefer diagrams as code. It keeps documentation honest. It makes developers want to work on documentation, because it looks like (and is) code. It allows one to take advantage of powerful open-source tools, such as git. It makes documentation portable across systems and over time.
