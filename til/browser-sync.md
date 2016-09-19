---
Date: 09/19/2016
Title: Use `browser-sync` as a proxy
Categories:
 - Node
Tags:
 - js
 - node
 - npm
 - proxy
---

# Use `browser-sync` as a proxy

I knew [`browser-sync`](https://www.browsersync.io/) was handy for working with static files, but what I didn't realize was that `browser-sync` had a proxy mode which will work with any framework.

```bash
$ npm install -g browser-sync
$ browser-sync start --files "_site/*" --proxy "localhost:8000" --reloadDelay "1000"
```

This is really handy for working with dynamic websites built with Django when you want to reload a page after you have made a template or CSS change. 
