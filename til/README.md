# Today I Learned (TIL)

02/15/2016 - PyEnv Py2 + Py3 System Wide (Python)
---
I thought I had a good grasp of pyenv but then I stumbled on: `pyenv global 2.7.11 3.4.3 3.5.1` which fixes my issue of how do I have Python 2 + Python 3 installed system wide.

02/17/2016 - Click Options Are Reusable (Python)
---
While researching ways to extend Click plug-ins, I stumbled on this [amazing tip](https://github.com/click-contrib/click-plugins/blob/master/README.rst#best-practices-and-extra-credit). Click options are reusable. I'm not sure why I never thought of this before but it's handy if you are writing dozens of click commands and you reuse the same options over and over. 

02/17/2016 - Py2 + Emoji + Encoding == Hard (:heart:)
---
It took me a while to wrap my brain around this. I'm getting a list of Emoji'zed Trello board names which I wanted to de-emoji so that it'll save happily in Sqlite3. Here was what finally did the trick: `emoji.demojize(board.name.decode('utf-8'))``
