# Python training for everyone

[0x00_conditionalsANdUseriput](./0x00_conditionalsANdUseriput): Writing basic Python that performs basic stuff.

[GAME FOR THE CLASS](./GAME_TIME/v1/) : game v1 let see how it works with conditionals

[0x01_loops](./0x01_loops/): STARTING UP LOOPS to expert'

[GAME FOR THE CLASS](./GAME_TIME/v2_GUESSING/) : game v2 let see how it works with conditionals, loops

[0x02_List-MethodANDSlice](./0x02_List-MethodANDSlice/) : LIST

## CODE FORMATTER
pycodestyle --first optparse.py // check your python code before push

```bash

pip install --upgrade pycodestyle
```

pycodestyle --show-source --show-pep8 testsuite/E40.py // show the source code for each error, and even the relevant text from PEP 8

pycodestyle --statistics -qq Python-2.5/Lib // you can display how often each error was found:

////// AUTO FORMATE

whenever u want to work with python
create .vscode // folder
create settings.json // file

//Paste below code

{
    "[python]": {
        "editor.defaultFormatter": "ms-python.autopep8"
    },
    "python. formatting.provider": "none"
}

// automatical style code Modules
to install

```bash

pip install --upgrade autopep8
```

autopep8 --in-place filename // it checks when pycodestyle did not see
