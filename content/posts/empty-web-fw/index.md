+++
linkTitle = "Empty Web Frameworks"
title = "Empty Web Frameworks"
draft = false
date = 2023-12-01
+++


| Framework | [Popularity](https://survey.stackoverflow.co/2023/#technology-most-popular-technologies) | New project size | # files | 
| :- | :- | -: | -: | 
| React | 1 | 340000K | 38219 | 
| htmx | \* | 44K | 1 |
| Angular | 5 | 295000K | 23757 | 
| Django | 13 | 20K | 9 |
| Gatsby | 24 | 542000K | 47703 | 
| jQuery | 3 | 88K | 1 |


\*: Not in top 34

## Methodology

### React

[Reference](https://create-react-app.dev/docs/getting-started/)

1. Install React (via npm)

```bash
> npm install react
> npm view react version
18.2.0
```

2. Create a project

```bash
> npx create-react-project empty-react-project
```

3. Analyze disk usage

```bash
> du -h -d 1 emptyDjangoProject 
  339M	empty-react-project/node_modules
   36K	empty-react-project/public
  368K	empty-react-project/.git
   32K	empty-react-project/src
  340M	empty-react-project
> find empty-react-project -type f | wc -l
   38219
```

### htmx

[Reference](https://htmx.org/docs/#installing)

1) Copy source code from CDN

*Note: htmx can be downloaded directly from a CDN inline with an html file, but for a fair comparison, the code was copied into a file so that the `du` disk utility could be run*

```bash
> mkdir empty-htmx-project
> curl -o emptyHtmxProject/htmx.min.js "https://unpkg.com/htmx.org@1.9.5/dist/htmx.min.js"
```

2) Analyze disk usage

```bash
> du -h emptyHtmxProject
 44K	emptyHtmxProject
```

### Angular

[Reference](https://angular.io/guide/setup-local)

1) Install Angular (via npm) 

```bash
> npm install -g @angular/cli
> npm view angular version
1.8.3
```

2) Create project

```bash
> ng new emptyAngularProject
? Would you like to enable autocompletion? Yes
? Would you like to share pseudonymous usage data about this project with the Angular Team? No
? Would you like to add Angular routing? Yes
? Which stylesheet format would you like to use? CSS
```

3) Analyze disk usage

```bash
> du -h -d 1 emptyAngularProject 
  294M	emptyAngularProject/node_modules
  336K	emptyAngularProject/.git
   12K	emptyAngularProject/.vscode
   56K	emptyAngularProject/src
  295M	emptyAngularProject
> find emptyAngularProject -type f | wc -l 
  23757
```

### Django

[Reference](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

1) Install Django

```bash
> python -m pip install Django
  Successfully installed Django-4.2.5
```

2) Create project

```bash
django-admin startproject emptyDjangoProject
```

3) Analyze disk usage

```bash
> du -h -d 1 emptyDjangoProject 
  16K	emptyDjangoProject/emptyDjangoProject
  20K	emptyDjangoProject
> find emptyDjangoProject -type f | wc -l 
  9
```

### jQuery

[Reference](https://jquery.com/download/)

*Note: Like htmx, jQuery can be downloaded directly from a CDN.

1) Copy source code from CDN

```bash
> curl -o emptyjQueryProject/jQuery.min.js "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"
```

2) Analyze disk usage

```bash
> du -h emptyjQueryProject 
  88K	emptyjQueryProject
```

### Gatsby

[Reference](https://www.gatsbyjs.com/docs/quick-start/)

1) Install Gatsby

```bash
> npm install -g gatsby-cli
> gatsby --version
Gatsby CLI version: 4.6.0
```

2) Create project

```bash
> npm init gatsby
? What would you like to call your site? emptyGatsbyProject
? What would you like to name the folder where your site will be created? empty-gatsby-project/
? Will you be using JavaScript or TypeScript? TypeScript
? Will you be using a CMS? No (or I'll add it later)
? Would you like to install a styling system? No (or I'll add it later)
? Would you like to install additional features with other plugins? No
```

3) Analyze disk usage

```bash
> du -h -d 1 empty-gatsby-project 
  540M	empty-gatsby-project/node_modules
  476K	empty-gatsby-project/.git
   24K	empty-gatsby-project/src
  542M	empty-gatsby-project
> find empty-gatsby-project -type f | wc -l  
  47703
```


