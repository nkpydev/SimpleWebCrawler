# SimpleWebCrawler
 Pythonic implementation of simple web crawler

## Idea:
    - Go to Target URL
    - Add it to Visited
    - Read all links present on target url and add them to To_Visit
    - Loop until To_Visit has no more records
    - Visited - will be end result with all Unique records of Links from Target URL

## Other Logics required:

    - URL should not be a static resource, e.g. image link, css link or JavaScript link
    - URL should not ending with /
    - URL should not be a # link

## How to run:

    
    python crawler.py


## To Do:

 - [x] Finish my changes
 - [ ] Add MultiThreading to process faster
 - [ ] Depth Control


## Author: 
[nkpydev](https://github.com/nkpydev)


## License:
[MIT](https://github.com/nkpydev/SimpleWebCrawler/blob/master/LICENSE)