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

[ ] Main Program Logic
[ ] Some basic crawler/indexers (Including Elastic Search)
[ ] Better Documentation (Guide to use and to build upon this)
[ ] Way to automatically get installed indexers/queries
[ ] More To Be Implimented Stuff
