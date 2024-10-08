# Project on hold
I'm sure your disappointed... Just getting back into the swing of things. Going to make a more straight forward implementation.

# watch-commander
Lightweight WebApp to lookup mass general laws and provide a single location for domestic violence, mental health, and OUI resources.
*Showcase for using flask and bootstrap*

# To get started:

Clone the repo:
https://github.com/kd1882/watch-commander.git

Get Python Poetry:
https://python-poetry.org/docs/

Installing Poetry:
Linux, macOS, Windows (WSL)
```
curl -sSL https://install.python-poetry.org | python3 -
```

Windows (Powershell)
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Ensure you add poetry to your path. Once that is all done, cd to the watch commander directory and:
```
poetry install
```
And all the dependencies will be installed.

You can then run the script via 
```
poetry run python3 server.py
```

or going into the shell
```
poetry shell

python3 server.py
```

# What's new?:

- Currently working on roughing in all the bootstrap for the mgl reference portion of the webapp. Then will tie everything together on the backend. Having a bit of an issue with the m.g.l api endpoint...

- Swapped scope of the project to simplify everything. Going to stick with what impacts police officers the most: Application of the laws, domestic violence, mental health, and OUI cases.

- Roughly got the code worked out to view MGL data, it works. Not good, better than it was.
    - Cleaned up the imports a bit, still working em.

### Current Branches:

- WC_002 
    - Identifying solution for having all of the M.G.L. laws (Chapter and Section) populate. Current working solution is to pull all the data and have it in the database.
