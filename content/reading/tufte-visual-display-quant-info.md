+++
linkTitle = 'Edward Tufte - The Visual Display of Quantitative Information (2001)'
title = 'Edward Tufte - The Visual Display of Quantitative Information (2001)'
shortTitle = 'Visual Display of Quantitative Information'
date = 2025-10-05T12:19:00-06:00
genres = ["reading", "2025"]
draft = false
+++

### 2) Graphical Integrity

> Much of the twentieth-century thinking about statistical graphics has been preoccupied with the question of how some amateurish chart might fool a naive viewer...At the core of the preoccupation was the assumption that data graphics were mainly devices for showing the obvious to the ignorant. It is hard to imagine any doctrine more likely to stifle intellectual progress in a field...Graphical excellence begins with telling the truth about the data. (*Graphical Integrity*, p. 54)

> Graphical Integrity is more likely to result if these six principles are followed: 
> 1) The representation of numbers, as physically measured on the surface of the graphic itself, should be **directly proportional to the numerical quantities represented**. 
> 2) **Clear, detailed, and thorough labeling** should be used to defeat graphical distortion and ambiguity. Write out explanations of the data on the graphic itself. **Label important events** in the data.
> 3) Show data variation, **not design variation**
> 4) In time-series displays of money, **deflated and standardized units of monetary measurement** are nearly always better than nominal units.
> 5) The number of information-carrying (variable) dimensions depicted [in a graphic] **should not exceed** the number of dimensions in the data.
> 6) Graphics must not quote data **out of context**.
> (*Graphical Integrity*, p. 77)

To me, this boils down to - proportionality, clarity, standardization, and context.

### 3) Sources of Graphical Integrity and Sophistication

> Many graphic artists believe that statistics are **boring and tedious**. It then follows that decorated graphics must pep up, animate, and all too often exaggerate what evidence there is in the data...[this] doctrine encourages placing data graphics under control of artists rather than in the hands of those who write the words and know the substance. (*Sources of Integrity and Sophistication*, p. 79-80)

> What E.B. White said of writing is also true of statistical graphics: "No one can write decently who is distrustful of the reader's intelligence, or whose attitude is patronizing." Contempt for graphics and their audience, along with the lack of quantitative skills among illustrators, has deadly consequences for graphical work: over-decorated and simplistic designs, tiny data sets, and big lies (*Sources of Integrity and Sophistication*, p. 81)

I have heard this opinion expressed by a number of individuals at the top of their craft. Bill Hicks once said to "play to the top of the room". To me, it manifests as a belief that my audience is always intelligent and discerning, and will not fall for BS in any form. Never patronize, and never hold contempt.

> I have compiled a rough measure of *graphical sophistication* - the share of a publication's graphics that are *relational*. Such a design links two or more variables but is **not a time-series or a map**...Relational graphics have been used since 1765 are printed billions of times and ways every year; and there is evidence that twelve-year-old children understand the design. (*Sources of Integrity and Sophistication*, p. 82)

> The audience for statistical graphics is smarter than many illustrators believe. (*Sources of Integrity and Sophistication*, p. 84)

> The conditions under which many data graphics are produced - lack of substantive and quantitative evidence, and contempt for the intelligence of the audience - guarantee graphic mediocrity....It wastes the tremendous communciative power of graphics to use them merely to decorate a few numbers.

> Surely there is something to be said for rejecting once and for all the doctrines that data graphics are for the unintelligent and that statistics are boring...graphical competence demands three quite different skills: the **substantive, statistical, and artistic**. (*Sources of Integrity and Sophistication*, p. 87)

#### 4) Data-Ink and Graphical Redesign

> Five principles in the theory of data graphics produce substantial changes in graphical design:
> 1) Above all else show the data.
> 2) Maximize the data-ink ratio.
> 3) Erase non-data-ink.
> 4) Erase redundant data-ink.
> 5) Revise and edit.
> (*Data-Ink and Graphical Redesign*, p. 105)

### 5) Chartjunk: Vibrations, Grids, and Ducks

This is the canonical Edward Tufte chapter, criticizing "chartjunk":

> The interior decoration of graphics generates a lot of ink that does not tell the viewer anything new. The purpose of decoration varies - to make the graphic appear more scientific and precise, to enliven the display, to give the designer **an opportunity to exercise artistic skills**. (*Chartjunk*, p. 107)

Chartjunk is what we may call resume-driven development in the software industry. A worker, lacking alternate outlets, seek to demonstrate competency by constructing complex, but ultimately useless decorations.

> There are better ways to portray spirits and essences than to get them all tangled up with statistical graphics...It is simply **graphical paraphernalia** routinely added to every display that passes by: over-busy grid lines and excess ticks, redundant representations of the simplest data, the debris of computer plotting, and many of the devices generating design variation. (*Chartjunk*, p. 107)

Three common types of *chartjunk* which Tufte elaborates on in this chapter are: **optical art** (e.g. moiré patterns), **grids** (as in, dark gridlines obscuring content), and **the graphical duck** (pure decorations)

#### Optical Art

Many examples in this section consist of unintentional optical illusions.

> Contemporary optical art relies on moiré effects, in which the design interacts with the physiological tremor of the eye to produce the distracting appearance of vibration and movement. (*Chartjunk: Vibrations, Grids, and Ducks*, p. 107)

> Moiré effects have proliferated with computer graphics (in programs such as Excel). Such unfortunate patterns were once generated by means of thin plastic transfer sheets; now the computer produces **instant chartjunk**. (*Chartjunk*, p. 111)


#### The Grid

Examples in this section consist of grid lines which obscure or distract from the underlying data.

> A gray grid works well and, with a delicate line, may promote more accurate data reconstruction than a dark grid...The reverse (unprinted) side [of ready-made graph paper] should be used, for then the lines show through faintly and do not clutter the data. (*Chartjunk*, p. 116)

#### The Graphical Duck

I am not totally sure I understand this point - I have rarely seen graphics that are purely decoration. Maybe Tufte was so effective in making this point, that we don't see this form of chartjunk much anymore.

My takeaway from this section is to refrain from decorations which obscure or distort the data. Most importantly, avoid decorations which serve to legitimize or increase the importance of the data. The data and numbers must be important only because they are actually important, not because of fancy graphical tricks.

> Forgo chartjunk, including moiré vibration, the grid, and the duck. (*Chartjunk*, p. 121)

### 6) Data-Ink Maximization and Graphical Design

> Erasing and data-ink maximizing have induced changes in the plain old bar chart. The techniques - no frame, no vertical axis, no ticks, and the white grid - apply to other designs [as well]. (*Data-Ink Maximization*, p. 129)

The suggestions here can apply to most data visualizations:

- Remove the frame
- Remove the vertical axis
- Remove tick marks
- Use a white grid (i.e. let the absence of ink communicate the grid lines)

> A useful fact, brought to notice by the maximization and erasing principles, is that the frame of a graphic can become an effective data-communicating element **simply by erasing part of it**. The frame lines should **extend only to the measured limits of the data**... (*Data-Ink Maximization*, p. 130)

In other words, instead of bounding the data with an arbitrary frame size, use a **range frame** - frame the data using only the precise x/y bounds which are needed for the data. This produces a **more informative** data visualization, with a greater focus on the **data**.

> Finally, the entire frame can be turned into data by framing the bivariate scatter with the **marginal distribution of each variable**. The *dot-dash-plot* results. (*Data-Ink Maximization*, p. 133)

> ...most of a graphic's ink should vary in response to data variation...The transformed designs are less cluttered and can be shrunk down more readily than the originals.

> Are transformed designs better?

> 1) ...more information per unit of space and per unit of ink is displayed.

> 2) ...editing, revision, and testing against different design options...suggest a direction in which revisions should move.

> 3) Then there is the audience...it is a frequent mistake to **underestimate the audience**. Instead, why not assume that if you understand it, most other readers will too? Graphics should be as **intelligent and sophisticated** as the accompanying text.

> 4) **With use**, the new designs will come to look just as reasonable as the old.

> There remain, however, many other considerations in the design of statistical graphics - not only of efficiency, but also of complexity, structure, density, and even beauty. (*Data-Ink Maximization*, p. 136-137)

Maximizing data-ink is only one goal, in other words.

### 7) Multifunctioning Graphical Elements

> Mobilize every graphical element, perhaps several times over, to show the data. (*Multifunctioning Graphical Elements*, p. 139)

These graphical elements include **data measures**, which is the ink that is communicating information about the underlying data. Numbers, points, bars, etc are all data measures. 

> The complexity of multifunctioning elements can sometimes turn data graphics into visual puzzles, **crypto-graphical mysteries** for the viewer to decode. A sure sign of a puzzle is that the graphic must be interpreted through a **verbal rather than a visual process**...in a non-puzzle graphic, the translation of visual to verbal is quickly learned, automatic, and implicit - so that the visual image flows right *through* the verbal decoder intiially necessary to understand the graphic. As Paul Valery wrote, "Seeing is forgetting the name of the thing one sees." (*Multifunctioning Graphical Elements*, p. 153)

The goal is for the data visualization to **flow**, and not need much explication.

### 8) High-Resolution Data Graphics

> Data-thin displays move viewers toward **ignorance and passivity**, and at times **diminish the credibility** of the source. Thin data displays rightly prompt suspicions that the display-makers have cherry-picked their data: "What are they leaving out? Is that all they know? Is that all the analytical work they did? Do they think we're fools? Why are we having this meeting?" (*High-Resolution Data Graphics*, p. 161)

> More information is better than less information, especially when the marginal costs of handling and interpreting additional information are low, as they are for most graphics...Maximize data density and the size of the data matrix, within reason (but at the same time exploiting the *maximum resolution* of the available data-display technology). (High-Resolution Data Graphics*, p. 166)

> The clutter of chartjunk, wasted space, non-data-ink, and redundant data-ink is **even more costly** than usual in data-rich designs. (*High-Resolution Data Graphics*, p. 167)

> Well-designed small multiples are inevitably comparative, deftly multivariate, shrunken, high-density graphics, usually based on a large data matrix drawn almost entirely with data-ink, efficient in interpretation, and often narrative in content... (*High-Resolution Data Graphics*, p. 169)

> These little data lines, because of their active quality over time, are named *sparklines* - small, high-resolution graphics usually embedded in a full context of words, numbers, images. Sparklines are *datawords*: **data-intense, design-simple, word-sized graphics**. (*High-Resolution Data Graphics*, p. 171)

I love this concept so much. I have always looked for an excuse to create/include sparklines in the UIs I've developed. I took a stab at a sparkline component in Django once, but never made a whole lot of progress on it. Maybe it's time to revisit the implementation, with my new HTMX and Alpine.js skills.

> Tables sometimes reinforce recency bias by **showing only current levels or recent changes**; sparklines improve the attention span of tables. (*High-Resolution Data Graphics*, p. 172)

> Readers can **scan** sparkline-tables, making simultaneous multiple comparisons, searching for nonrandom patterns in the random walks of prices. (*High-Resolution Data Graphics*, p.173)

> Sparklines efficiently **display and narrate binary data** (presence/absence, occurrence/non-occurrence, win/loss)...(*High-Resolution Data Graphics*, p. 174)

> The datawords of sparklines vastly increase the amount of data **within our eyespan**. Operating at the resolution of good typography, sparklines can be **everywhere a number of word can be**..By providing a straightforward and contextual look at intense evidence, sparklines may help us, in John Tukey's words, to find an approximate answer to the right question (rather than **an exact answer to the wrong question**)...**For non-data-ink, less is more. For data-ink, less is a bore**. (High-Resolution Data Graphics, p. 175).

Fantastic section. The idea of sparklines was very influential on me when I first started my career, and was developing webpage UIs and data visualizations in Tableau and PowerBI.

### 9) Aesthetics and Technique in Data Graphical Design

> Graphical elegance is often found in simplicity of design and complexity of data...The best graphics are about the useful and important, about life and death, about the universe. Beautiful graphics **do not traffic with the trivial**. (Aesthetics and Technique, p. 177)

> Attractive displays of statistical information:
> - have a properly chosen format and design
> - use words, numbers, and drawing **together**
> - reflect a balance, a proportion, a sense of relevant scale
> - display an **accessible complexity** of detail
> - often have a narrative quality, a **story** to tell about the data
> - are drawn in a **professional manner**, with the technical details of production done with care
> - avoid content-free decoration, including **chartjunk**

I love the phrase **accessible complexity**. It's analogous to progressive disclosure, a feature of programming languages such as Go. The audience can get something from the surface-level of the graphic, but if they peer deeper (or have deeper knowledge of the subject), they can understand even more. This encourages the audience to rise to the level of the graphic, rather than you patronizingly *descending* to what you think is their level. I feel like I must disagree with most developers or designers on this subject, because many UIs and technologies presume that their audience is stupid.

> Words and pictures are sometimes jurisdictional enemies, as artists feud with writes for scarce space. An unfortunate legacy of these craft-union differences is the artificial separation of words and pictures; a few style sheets even forbid printing on graphics. (*Aesthetics and Technique*, p. 180)

> Data graphics are **paragraphs about data** and should be treated as such...Tables and graphics should be run into the text whenever possible, avoiding the clumsy and diversting segregation of "See Fig. 2," (figures all too often located on the back of the adjacent page). (*Aesthetics and Technique*, p. 181)

> An occasional data graphic displays such care in design that it is particularly accessible and open to the eye, as if the designer **had the viewer in mind at every turn** while constructing the graphics. This is the *friendly data graphic*. (*Aesthetics and Technique*, p. 183)

> ...it should be realized that words consisting of only capital letters present the most difficult reading - because of their equal height, equal volume, and, with most, their equal width. When comparing serif letters with sans-serif, the latter provide an **uneasy reading**. The fashionable preference for sans-serif in text shows neither historical nor practical comeptence. (*Aesthetics and Technique*, p. 183)

Avoid ALL CAPS, and avoid sans-serif, at least if you are interested in making it easy for people to read what you wrote.

### Epilogue: Designs for the Display of Information

> The theory of the visual display of quantitative information consists of principles that generate design options and that guide choices among options. The principles should not be applied rigidly or in a **peevish** spirit; they are not logically or mathematically certain; and it is better to **violate any principle than to place graceless or inelegant marks on paper**. Most principles of design should be greeted with some skepticism, for **word authority** can dominate our vision, and we may come to see only through the lenses of word authority rather than with our own eyes.
> What is to be sought in designs for the display of information is the **clear portrayal** of complexity. Not the **complication of the simple**; rather the task of the designer is to give visual access to the subtle and the difficult - that is, **the revelation of the complex**. (*Epilogue*, p. 191)
