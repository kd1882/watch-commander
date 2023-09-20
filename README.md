# watch-commander
Lightweight WebApp to lookup mass general laws, post shift notes.

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

### Needs done:
- users stuff
    - update users to add and store a photo
        - change account info toggle
        - add delete account functionality

- keep me logged in functionality
- forgot password functionality

- add user posted for role call notes
    - add filtering by date

- department info
    - add way to update, photo for department, acl?

- contact the devs form adds a ticket to a database?

- add FAQ's

- populate mgl data for database
    - table for mgl chapter
    - page for chapter/section 

- fix styling on pages
    - dashboard_base - 100% of viewport, fixed pos, contact the devs fixed pos, 
    - scrolling only affects the content portion of th page
