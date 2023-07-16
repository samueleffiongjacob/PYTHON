# I BEGIN MY JOUNERY AGAIN IN PYTHON FULL TO UNDERSTAND FULL CONCERPT

[DAY1](./DAY_1) : Writing basic python that perform basic stuff.
[GAME FOR THE CLASS](./GAME_TIME/v1/) : game v1 let see how it works with conditionals
[DAY2](./DAY_2/) : STARTING UP LOOPS'
[GAME FOR THE CLASS](./GAME_TIME/v2_GUESSING/) : game v2 let see how it works with conditionals, loops
[DAY3](./DAY3/) : LIST

## CODE FORMATTER
pycodestyle --first optparse.py // check your python code before push

```bash

pip install --upgrade pycodestyle
```

pycodestyle --show-source --show-pep8 testsuite/E40.py // show the source code for each error, and even the relevant text from PEP 8

pycodestyle --statistics -qq Python-2.5/Lib // you can display how often each error was found:

////// AUTO FORMATE

when ever u want to work with python
create .vscode // folder
create settings.json // file

// paste below code

{
    "[python]": {
        "editor.defaultFormatter": "ms-python.autopep8"
    },
    "python.formatting.provider": "none"
}

// autamaatical style code Modules
to install

```bash

pip install --upgrade autopep8
```

autopep8 --in-place filename // it checks whe pycodestyle did not see
