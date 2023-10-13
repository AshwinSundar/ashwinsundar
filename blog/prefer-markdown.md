# Prefer Markdown

October 2023

I have spent a lot of time writing HTML. I wrote my first HTML when I was around 12. I'm not trying to brag - I was obsessed with a website called `neopets.com`, a website geared for kids to take care of virtual pets. There were games to play, coins to earn, and pets to splurge on. Items could be earned and sold in a "shop" to other players (for fake currency only). I wanted to customize my Neopets shop, which was allowed using this thing called "HTML". I had just learned to type, and was pretty good at Mavis Beacon at school.

<img src = "/blog/assets/prefer-markdown/neopets-html.png" style="display: block; margin: auto; width: 90%" />
<figcaption style = 'text-align: center'>Thank you, Neopets, for not changing the style of this page for 20 years.</figcaption>

In college, I took advantage of self-hosting provided by the school to share my photography. Thank you, Wayback Machine, for keeping [this snapshot](https://web.archive.org/web/20131122205041/http://ashiundar.bol.ucla.edu/).

Recently, I re-wrote my entire personal website in raw HTML and about 20 lines of CSS. This site is remarkably simple by modern web standards - feel free to hit "Inspect" and peer at what's going on. It's not much.

## HTML?  

Frankly, I don't get the appeal. Writing HTML doesn't make me feel nostalgic.  

Rather, I feel the weight of old technologies dragging me down. It's really, really hard to enter a state of "writing flow" when you have to constantly remember to close out HTML tags. The effect of forgetting a single `/>` is that the entire page looks like shit. Debugging the style of an HTML file is one of the most thoroughly uninteresting programming experiences a developer can have.

Markdown has been my favorite markup language for the last several years. A raw Markdown file is very human-readable. In Markdown, there are few formatting rules that must be followed. Compare this with the tag detritus scattered about a standard HTML file.  


<img src = "/blog/assets/prefer-markdown/html-vs-md.png" style="display: block; margin: auto; width: 100%"/>
<figcaption style = 'text-align: center'>HTML vs Markdown. Which is easier to read? Yes, that's the high contrast theme in VSCode. Yes, I use VSCode to write articles. Yes, I have vim-mode enabled.</figcaption>

Additionally, HTML can be embedded in Markdown. So if one really does need custom styling, raw HTML is still available as a fallback. That image and caption above? 

```HTML
<img src = "/blog/assets/prefer-markdown/html-vs-md.png" style="display: block; margin: auto; width: 100%" />
<figcaption style = 'text-align: center'>Which is easier to read? Yes, that's the high contrast theme in VSCode. Yes, I use VSCode to write articles. Yes, I have vim-mode enabled.</figcaption>
```

This is the raw HTML, embedded in-line with all this Markdown around it. I do not know the extent to which the full HTML spec is supported in Markdown. However, I have yet to encounter a situation that could not be served by reverting to HTML briefly.

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

1) Markdown to HTML conversion is dead simple.

2) Writing in markdown reduces cognitive load by a significant amount, compared to writing in HTML. This allows a writer to remain "in flow" much more easily.  