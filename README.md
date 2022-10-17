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

# GH Pages Site (No Jekyll)
> Template for a Markdown-based docs site hosted on GH Pages

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/gh-pages-no-jekyll?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/gh-pages-no-jekyll/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

Write Markdown or HTML pages and use GitHub's default theme for your site. No configuration needed. All you need is HTML, Markdown, and CSS knowledge - no need to use Jekyll templating or Liquid syntax.


## Preview


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


<div align="center">

[![View site - GH Pages](https://img.shields.io/badge/View_site-GH_Pages-blue?style=for-the-badge)](https://michaelcurrin.github.io/gh-pages-no-jekyll/)

[![Use this template](https://img.shields.io/badge/Use_this_template-Generate-2ea44f?style=for-the-badge)](https://github.com/MichaelCurrin/gh-pages-no-jekyll/generate)

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
