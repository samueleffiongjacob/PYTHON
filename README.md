# Python training for everyone

[0x00_conditionals ANd User iput](./0x00_conditionalsANdUseriput): Writing basic Python that performs basic stuff.

[GAME FOR THE CLASS](./GAME_TIME/v1/) : game v1 let see how it works with conditionals

[0x01_loops](./0x01_loops/): STARTING UP LOOPS to expert'

[GAME FOR THE CLASS](./GAME_TIME/v2_GUESSING/) : game v2 let see how it works with conditionals, loops

[0x02_List-Method AND Slice](./0x02_List-MethodANDSlice/) : LIST

## CODE FORMATTER
autopep8 2.0.2 : A tool that automatically formats Python code to conform to the PEP 8 style guide [SEE DOCUMENTATION](https://pypi.org/project/autopep8/)

```bash
# Install  Autopep8
$ pip install --upgrade autopep8

# It checks when pycodestyle did not see
$ autopep8 --in-place pythonfile 
```
pycodestyle is a tool to check your Python code against some of the style conventions in PEP 8. [SEE Documentation](https://pypi.org/project/pycodestyle/)

```bash
# To install PYCODESTYLE
$ pip install --upgrade pycodestyle

# check your Python code before pushing
$ pycodestyle  python file

# show the source code for each error and even the relevant text from PEP 8
$ pycodestyle --show-source --show-pep8  python file

# You can display how often each error was found:
$ pycodestyle --statistics -qq Python-2.5/Lib 
```


```bash

# AUTO FORMATE with VS code

# whenever you want to work with python create vs code folder example below
$ .vscode

# Inside the folder create a setting.json file example below
$ settings.json

# Paste the below code inside your setting.json file

    {
    "[python]": {
        "editor.defaultFormatter": "ms-python.autopep8"
    },
    "python. formatting.provider": "none"
}

```


