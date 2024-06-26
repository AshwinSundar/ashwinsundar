+++
linkTitle = "Prefer Markdown"
shortTitle = "Prefer Markdown"
title = "Prefer Markdown"
draft = false
genres = ["technical"]
date = 2023-10-01
+++

I have spent a lot of time writing <span class = "definition" data-def = "Hypertext Markup Language">HTML</span>. I wrote my first <span class = "definition" data-def = "Hypertext Markup Language">HTML</span > when I was around 12 years old. I was obsessed with a website called `neopets.com`, a website geared for kids to take care of virtual pets. There were games to play, coins to earn, and pets to splurge on. Items could be earned and sold in a "shop" to other players (for fake currency only). I wanted to customize my Neopets shop, which was allowed using this thing called <span class = "definition" data-def = "Hypertext Markup Language">"HTML"</span>.  This seemed like a fun way to test out these new typing skills I learned from [Mavis Beacon Teaches Typing](https://en.wikipedia.org/wiki/Mavis_Beacon_Teaches_Typing).

![Neopets](./neopets-html.png)
*Thank you, Neopets, for not changing the style of this page for 20 years.*

In college, I took advantage of self-hosting provided by the school to share my photography. I created some HTML files, uploaded images, and told the server where to find them. Thank you, Wayback Machine, for keeping [this snapshot](https://web.archive.org/web/20131122205041/http://ashiundar.bol.ucla.edu/).

Recently, I re-wrote my entire personal website in raw HTML and about 20 lines of CSS. This site is remarkably simple by modern web standards - feel free to hit "Inspect" and peer at what's going on. It's not much.

## <span class = "definition" data-def = "Hypertext Markup Language">HTML</span>?  

Frankly, I don't get the appeal. Writing <span class = "definition" data-def = "Hypertext Markup Language">HTML</span> doesn't make me feel nostalgic.  

Rather, I feel the weight of old technologies dragging me down. It's really, really hard to enter a state of "writing flow" when you have to constantly remember to close out <span class = "definition" data-def = "Hypertext Markup Language">HTML</span> tags. The effect of forgetting a single `/>` is that the entire page looks like shit. Debugging the style of an <span class = "definition" data-def = "Hypertext Markup Language">HTML</span> file is one of the most thoroughly uninteresting programming experiences a developer can have.

Markdown has been my favorite markup language[^markup-def] for the last several years. A raw Markdown file is very human-readable. In Markdown, there are few formatting rules that must be followed. Compare this with the tag detritus scattered about a standard <span class = "definition" data-def = "Hypertext Markup Language">HTML</span> file.  

![HTML vs Markdown](html-vs-md.png)
*HTML vs Markdown. Which is easier to read? Yes, that's the high contrast theme in VSCode. Yes, I use VSCode to write articles. Yes, I have vim-mode enabled.*

Additionally, <span class = "definition" data-def = "Hypertext Markup Language">HTML</span> can be embedded in Markdown. So if one really does need custom styling, raw <span class = "definition" data-def = "Hypertext Markup Language">HTML</span> is still available as a fallback. That image and caption above? This is the raw <span class = "definition" data-def = "Hypertext Markup Language">HTML</span>, embedded in-line with all this Markdown around it:

```HTML
<img src = "/blog/assets/prefer-markdown/html-vs-md.png" style="display: block; margin: auto; width: 100%" />
<figcaption style = 'text-align: center'>Which is easier to read? Yes, that's the high contrast theme in VSCode. Yes, I use VSCode to write articles. Yes, I have vim-mode enabled.</figcaption>
```

I do not know the extent to which the full <span class = "definition" data-def = "Hypertext Markup Language">HTML</span> spec is supported in Markdown. However, I have yet to encounter a situation that could not be served by reverting to <span class = "definition" data-def = "Hypertext Markup Language">HTML</span> briefly.

Of course, Markdown can't be published directly as a static page. Browsers don't know how to read Markdown. One would think that this requires the use of a complex tool to convert from human-speak to browser-speak - but no! A simple bash script and a handy tool called *pandoc* is all you need:

```bash
mdToHtml {
    files=$(find blog -name "*.md")
    for f in $files; do
        pandoc -f markdown $f > blog/compiled/$(basename "${f%.*}").html
    done
}
```

"Done" is right! What about templates?

```bash
mdToHtml2() {
    files=$(find blog -name "*.md")
    for f in $files; do
        pandoc -f markdown $f > blog/$(basename "${f%.*}").html
        head=$(head -n10 templates/blogTemplate.txt) # first n = 10 lines, header up to <body>
        tail=$(tail -n2 templates/blogTemplate.txt) # last n = 2 lines, </body></html>
        echo $head | cat - blog/$(basename "${f%.*}").html > temp && mv temp blog/$(basename "${f%.*}").html
        echo $tail >> blog/$(basename "${f%.*}").html
    done
    echo "Markdown files converted to HTML"
}
```

Yes, that script is verbose and not optimized for organization. I don't remember why it writes to a temp file first. The styling on this site has issues. But it gets the job done.

## To summarize

1) Markdown to <span class = "definition" data-def = "Hypertext Markup Language">HTML</span> conversion is dead simple.

2) Writing in Markdown reduces cognitive load, enabling a writer to remain "in flow" much more easily.  

[^markup-def]: A [markup language](https://en.wikipedia.org/wiki/Markup_language) is used to control the display of a document. Common examples include <span class = "definition" data-def = "Hypertext Markup Language">HTML</span>, Markdown, and LaTeX.
