+++
linkTitle = "Cheap Web Scorecard"
title = "Cheap Web Scorecard"
draft = false
date = 2023-12-01
+++

I recently came across [The "Cheap" Web](https://potato.cheap/), a self-described "solarpunk philosophy of web design". I highly recommend reading the whole article, for it's both a throwback to what the web used to be, as well as a vision for what the future may hold.

Towards the end of the article, the author proposes the following measures of cheapness. I decided to rate this website according to those measures.

## Cheap to maintain

**Definition**: _Most webpages should work indefinitely without falling over._

**Rating: 9/10**

This website uses 0 lines of Javascript. It is composed entirely of HTML and styled with a little bit of CSS. I write articles in Markdown, which are compiled to HTML using a custom shell script that I maintain. For deployment, I push to GitHub, where changes are picked up by a DigitalOcean static-file-deployment application. 

If DigitalOcean were to fall over tomorrow, it would probably take about half a day to either migrate to a new provider, or set up self-hosting. Given that this is the only potential source of failure I see for the next several years, I'd say this site is doing pretty well on this metric. 4 hours of downtime is not a big deal, because no one visits this site, like, ever[^visits].

## Cheap to leave  

**Definition**: _Opting-out of the web should be painless._

**Rating: 10/10**

How to leave this website:

1) Click the [X] in the top right (or top left on macos)  
2) Go outside.  

## Cheap to access

**Definition**: _Most websites should be compatible with screenreaders, etc._

**Rating: 8/10** 

Reader-view looks pretty good for the blog posts. I think I missed a few `<alt>` tags for images here and there though. I don't know how to make `<audio>` tags compatible with a screenreader. And the index page doesn't seem to be reader-friendly for some reason.

## Cheap to participate  

**Definition**: _Interacting with the web should be possible on a Wii._

**Rating: 10/10**

[Lynx](https://en.wikipedia.org/wiki/Lynx_(web_browser)), a terminal-based web browser that predates Mosaic, is still alive and kicking. Here's what this site looks like:  

```shell
> lynx www.ashwinsundar.com
```
![ashwinsundar.com in Lynx 2023](lynx.png)

*ashwinsundar.com in Lynx 2023*

That's pretty usable. Someone with the cheapest computer and slowest internet connection can still read my inane thoughts and musings.

## Cheap to explore

**Definition**: _Exploring the web should be pleasant on 1W of power._

**Rating: ?/10**

I don't own a computing device that runs on 1W of power. The Energy tab in macos's Activity Monitor shows this:

![florbs of power used by ashwinsundar.com](energy.png)
*Florbs of power used by ashwinsundar.com*

Helpfully, Apple decided that including units in this table was too confusing for the average Mac user. So we are only left to wonder how many units of energy Firefox uses when it is opened to this site.

## Cheap to contribute

**Definition**: _Making/hosting websites should be easier than scrapbooking._

**Rating: 10/10**  

https://github.com/AshwinSundar/ashwinsundar.github.io

Feel free to submit a PR. 

## Summary 

| Criterion | Rating |
| - | - |
| Cheap to maintain | 9/10 | 
| Cheap to leave | 10/10 |
| Cheap to access | 8/10 |
| Cheap to participate | 10/10 |
| Cheap to explore | 🐟/10 |
| Cheap to contribute | 10/10 |
| Overall | (47 + 🐟) / 6 |

The main takeaway is that the simplicity of this site enabled it to score well on this "Cheap Web" scorecard. In the areas that could be rated, it averaged a 9.4/10. This site could use improvements in the area of accessibility, which will be very easy to make thanks to how simple the site is.  

[^visits]: I assume this is true, but I don't track page visits. Or track anything for that matter
