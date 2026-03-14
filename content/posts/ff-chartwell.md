+++
linkTitle = 'Chartwell and Tailwind CSS'
title = 'Chartwell and Tailwind CSS'
shortTitle = 'Chartwell'
date = 2026-03-14T14:00:08-06:00
genres = ['technical']
draft = false
audioFile = ""
audioTitle = ""
+++

I finally decided to purchase a license for Chartwell, a typeface that takes advantage of [OpenType's discretionary ligatures feature](https://helpx.adobe.com/fonts/using/open-type-syntax.html#dlig) to render custom shapes. In Chartwell's case, this enables the display of inline graphs and charts, otherwise known as [**sparklines**](https://www.edwardtufte.com/notebook/sparkline-theory-and-practice-edward-tufte/).

>> Sparklines...are small, high-resolution graphics usually embedded in a full context of words, numbers, images. Sparklines are *datawords*: data-intense, design-simple, word-sized graphics. (*Beautiful Evidence* p. 47, Edward Tufte, 2006)

<figure>
  <img
  src="/images/chartwell/sparklines-tufte-1.jpeg"
  alt="An example of sparklines for personal healthcare data">
  <figcaption><i>Beautiful Evidence, p. 47</i></figcaption>
</figure>
<br>

<figure>
  <img
  src="/images/chartwell/sparklines-tufte-2.jpeg"
  alt="Another example, this time with research data for mouse neuronal activity">
  <figcaption><i>Beautiful Evidence, p. 55</i></figcaption>
</figure>
<br>

An incredible amount of information can be compressed into a simple squiggle. Chartwell repurposes typographical graphemes to provide a language of data verbs.

Early in my career, a colleague gifted me an Edward Tufte book called **Envisioning Information**, which has remained very formative and important to my career, specifically when creating user interfaces and visualizatons. The sparkline is one of the most memorable concepts I learned from the book. 

For years, I have wanted to create a front-end utility or library to make the generation of sparklines intuitive, but never could come up with an easy-enough implementation to make them perfectly seamless to render with text. The best solution I could think of was to embed SVGs inline with text, but this is messy and painful to implement.

The idea of pushing sparkline rendering down one level, into the font itself, was not something I was aware was possible. Travis Kochel, a designer and font expert, figured this out using OpenType's discretionary ligatures feature and pioneered FF Chartwell (now called Vectra Chartwell, or just Chartwell). I recently added Chartwell to the [animal colony management software](https://mousehouse.bio), and was excited to see my first sparkline in a creation of mine! Here's how I added it to a Django web application using the Tailwind CSS styling framework.

1) Purchase the font asset files from [Vectro](https://www.vectrotype.com/chartwell). 
Yeah it's not free...alternatively, you can roll your own font with custom discretionary ligatures, if you happen to be so skilled and have so little value for your time. I wasted a year envying this library and thinking of ways to replicate it, when I could have been using it and enjoying it that whole time.

2) Copy the `.woff2` font files to your `/static/fonts` directory

There are 15 different types of charts available, and several sub-variations. Every chart and subvariation has its own `.woff2` file. Don't worry about bloating your web page - Django (and most web frameworks) are smart enough to only load the fonts and resources required for the particular page the user is currently on.

3) Update `styles.css`

Tailwind has to know where the files are. You need to also set `font-feature-settings` such that discretionary ligatures (`dlig`) are enabled. It makes the most sense to enable that setting globally at the font level, instead of remembering to apply this very weird CSS attribute to every component that uses Chartwell.

If you don't do this, then any visualizations that you try to render with Chartwell will only have the font style applied, but not actually be converted into the appropriate charts. So you'll see something the literal values that you entered (e.g. `40+30+70`), rather than the chart itself.

```css
@config "../../tailwind.config.js";
@import "tailwindcss";
@plugin "@tailwindcss/forms";
@plugin "@tailwindcss/typography";
@plugin "@tailwindcss/aspect-ratio";
@tailwind base;
@tailwind components;
@tailwind utilities;

@font-face {
    font-family: 'Chartwell Arcs';
    src: url('../fonts/Chartwell-Arcs.woff2') format("woff2");
    font-feature-settings: "dlig" 1;
}

@font-face {
    font-family: 'Chartwell Areas';
    src: url('../fonts/Chartwell-Areas.woff2') format("woff2");
    font-feature-settings: "dlig" 1;
}

@font-face {
    font-family: 'Chartwell Areas Ranges';
    src: url('../fonts/Chartwell-AreasRanges.woff2') format("woff2");
    font-feature-settings: "dlig" 1;
}

@font-face {
    font-family: 'Chartwell Bars';
    src: url('../fonts/Chartwell-Bars.woff2') format("woff2");
    font-feature-settings: "dlig" 1;
}

...repeat for remaining Chartwell fonts
```

4) Update `tailwind.config.js`

I'm still using a [config.js](https://v3.tailwindcss.com/docs/configuration) file for Tailwind CSS, which I guess they dropped support for in Tailwind v4. In any case, for Tailwind v3, add a `fontFamily` object inside of `module.exports.theme` with a list of all the Chartwell fonts.

```css
module.exports = {
  theme: {
    fontFamily: {
      'chartwell-arcs': ['"Chartwell Arcs"'],
      'chartwell-areas': ['"Chartwell Areas"'],
      'chartwell-areas-ranges': ['"Chartwell Areas Ranges"'],
      'chartwell-bars': ['"Chartwell Bars"'],
      ...repeat for remaining charts
    },
  },
};
```

5) Rebuild Tailwind

I use the Tailwind CLI, so the command is `./tailwindcss -i ./static/css/styles.css -o ./static/css/styles.out.css`. I also re-gather the static files and drop them in a `collectedstatic` folder[^poor-naming] using the command `.venv/bin/python3 manage.py collectstatic --no-input`. 

---

If things have gone well, you are now able to apply a Tailwind class called `font-chartwell-lines-a` to a `<span>`, and use the appropriate syntax for the chart-type to generate this:

```html
    <span>This is a sparkline! </span><span class="font-chartwell-lines-a" title="Lines A">40+80+55+20+60</span><span>I can type text afterwards and it sits nicely inline.</span>
```

<figure>
  <img
  src="/images/chartwell/sparkline-1.png"
  alt="Your first sparkline!">
  <figcaption><i>A native font sparkline!</i></figcaption>
</figure>
<br>

Let's look at some more interesting examples...eventually. There is so much potential here. Buy an Edward Tufte book to see a bunch of examples of sparklines and let the ideas flow from there.

[^poor-naming]: This isn't the best name for the static folder, but I made it when I was first learning Django, and I thought it made sense to just give it a fresh name. Oh well. Lesson learned.
