---
permalink: /
---
<style>
/* from here: https://blog.devgenius.io/word-cloud-with-html-and-css-tutorial-1fa17642391e*/
body {
    /* center content */
    position: absolute;
    top:0;
    bottom: 0;
    left: 0;
    right: 0;
    /* grid */
    display: grid;
    justify-content: center;
    align-content: center;
    gap: 5px;
    /* A grid-template is a shorthand for defining the layout similar to excel format only here each row is made of text containing
    name references to objects (in our case it’s the “grid-area” or empty cells defined as “.”) separated by spaces. */
    grid-template:
    '. . . Information Documentation Documentation Documentation Documentation'
    'Computer Computer Computer Information Coding Debugging Learning Testing'
    '. Readability Software Information Coding Debugging Learning Design     '
    '. . Software Information Programming Debugging Learning Design'
    '. . Software Information Algorithm Debugging Learning Design'
    '. . . Information . . Learning .';

}
body > div {
    text-shadow: 3px 5px 8px rgba(1, 1, 1, 0.3);
}
/* base font color for all words */
body > div {
    color: #022f40;
}
/* twice the size, bold and different color for each second word */
body :nth-child(2n) {
    font-size: 2rem;
    color: #38aecc;
    font-weight: bold;
}
/* vertical orientation and different color for each third word */
body :nth-child(3n) {
    writing-mode: vertical-lr;
    -webkit-writing-mode: vertical-lr;
    -ms-writing-mode: vertical-lr;
    color: #0090c1;
}
/* triple size and different color for each fourth word */
body :nth-child(4n) {
    font-size: 3rem;
    color: #183446;
}
/* quadruple size and different color for each fifth word */
body :nth-child(5n) {
    font-size: 4rem;
    color: #046e8f;
}

#Programming {
    grid-area: Programming;
}
#Algorithm {
    grid-area: Algorithm;
}
#Software {
    grid-area: Software;
}
#Documentation {
    grid-area: Documentation;
}
#Coding {
    grid-area: Coding;
}
#Information {
    grid-area: Information;
}
#Testing {
    grid-area: Testing;
}
#Computer {
    grid-area: Computer;
}
#Debugging {
    grid-area: Debugging;
}
#Design {
    grid-area: Design;
}
#Readability {
    grid-area: Readability;
}
#Learning {
    grid-area: Learning;
}
</style>
# **Documentation**
> How this project works and how to maintain your own

    <div id="Programming"> Programming</div>
    <div id="Algorithm"> Algorithm</div>
    <div id="Software"> Software</div>
    <div id="Documentation"> Documentation</div>
    <div id="Coding"> Coding</div>
    <div id="Information"> Information</div>
    <div id="Testing"> Testing</div>
    <div id="Computer"> Computer</div>
    <div id="Debugging"> Debugging</div>
    <div id="Design"> Design</div>
    <div id="Readability"> Readability</div>
    <div id="Learning"> Learning</div>




## About

This project is built around using markdown content to make a website. 

This is great for non-developers to work on. No experience with Ruby, Jekyll, Liquid, HTML or CSS required. Those are all used internally, but you don't need to worry about that.

This repo is super light. No config needed. You don't need to setup a theme or a layout. GitHub will figure that out and will apply its standard theme to your GitHub Pages site. So will it will have a clean, white, mobile-friendly site with a heading. The limitations are covered more on these pages, such as lack of a navbar. But you can still setup links to pages, as with the Menu below.

The page you are currently viewing is `README.md` in the docs directory, with path set as `/` in the frontmatter. Alternatively, you can add `index.md` or `index.html` as your homepage. I just like how a README.md previews well in GitHub.


## How to use this project

- Template for a new project or docs site. Or use as a reference for existing projects.
- Read the tutorial content under template notes.
- View this live demo site.


## Menu

Some info on how to make a site like this and how it works.

- [About](about.md)
- [Features](features.md)
- [Limitations](limitations.md)
- [What about a Wiki?](wiki.md)


## Source

View source on GitHub:

[![MichaelCurrin - gh-pages-no-jekyll](https://img.shields.io/static/v1?label=MichaelCurrin&message=gh-pages-no-jekyll&color=blue&logo=github)](https://github.com/MichaelCurrin/gh-pages-no-jekyll)


## Documentation template

If you're looking for template docs which you can easily edit and reuse for your own site, rather see my [Generic Project Template](https://michaelcurrin.github.io/generic-project-template/) project's docs. It uses the same docs site approach as this one.

