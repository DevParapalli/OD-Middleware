# OD-Middleware

## Introduction

Pretty much WIP. More documentation incoming.


## Contributors Notes:

I am a 12th Year Student, Not much time could be invested by me.
Contributions are very welcome. Feel Free to correct my code, just make sure you don't break other parts of the codebase while doing this. 
I will be able to add small bits to this. The code is supposed to be used as a middleware, not a be-all or end-all solution, will try to get at-least a CLI or something.

a service should be named such that it can be imported into python using importlib, in short keep it ascii text only.
ie, odcrawler.xyz should be renamed as odcrawler_xyz.py

The functionality should be exposed as a `queries.service.process` function. The function should accept a `classes.Query` and return a list containing the result in a specified format (explained in `queries.example.unified_format`).

## To Be Implimented

- [ ] Main Program Logic
- [ ] Some basic crawler/indexers (Including Elastic Search)
- [ ] Better Documentation (Guide to use and to build upon this)
- [ ] Way to automatically get installed indexers/queries
- [ ] More To Be Implimented Stuff

## Extractors/Queries WIP

- This is a list of indexers I am planning to implement, Contact RogueCatalyst (HASH) 4144 over at Discord to add more. I am not very good with GitHub PRs and Git Merges.If someone can guide me or link me to a guide, it would be appreciated.

Credit : u/GrowAsguard at r/opendirectories, [Post Here](https://www.reddit.com/r/opendirectories/comments/lj0a1e/my_favorite_open_directory_search_tools/)

Search And index Engines DDLs :-
<https://filepursuit.com/>
<https://weboas.is/>
<https://filesearch.link/>
<https://ipfs-search.com/>

Search GDrive:-
<https://www.dedigger.com/>
<https://whatintheworld.xyz/>
<https://w3abhishek.github.io/torrentables/>
<https://eyedex.org/> (Search The Eye)

Search Open Directory DDLs :-
<https://odcrawler.xyz/>
<https://www.filechef.com/>
<https://opendirsearch.abifog.com/>
<http://palined.com/search/>
<https://ewasion.github.io/opendirectory-finder/>
<https://open-directories.reecemercer.dev/>
<https://lumpysoft.com/>
<https://www.eyeofjustice.com/od/>
<https://sites.google.com/view/l33tech/tools/ods>
<http://lendx.org/>

Archiving And Searching Engines:-
<https://the-eye.eu/> (archives and indexes Web Pages)
<http://archive.ph/> (archives web snapshots)
<https://archive.org/> ( The Internet Archive)
<https://archive.org/web/> (The Wayback Machine)

FTP Indexers:-
<https://www.mmnt.ru/int/>
<https://www.catfiles.net/>
<https://sites.google.com/view/l33tech/tools/pasteskimmer> (Paste search tool)

Multiple torrent sites search :-
<https://filelisting.com/>
<https://solidtorrents.net/>
<https://torrents-csv.ml/>

Indexes from the comments.
<https://gist.github.com/Krazybug/5f015c2ee7e39b3faff08d1d1d91f802>
<https://calishot-eng-2.herokuapp.com/index-eng/summary>
<https://calishot-eng-4.herokuapp.com/index-eng/summary>
<http://torrbot.com/>