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