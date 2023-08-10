# Debugging and Error Handling

## Objectives

> Exaplain common errors and how they occur in python  
> Use pdb to set breakpoints and steps through code  
> Use try and Except blocks to handle errors  

## SOME COMMON ERRORS

> SyntaxError:
  Occurs When python encounters incorrect syntax(Something it doesn't parse)
  Usually due to typo or not knowing python well enough

  ```bash
    # example
    $ def first # SyntaxError: invalid syntax no ':' 
    $ None = 1 # SyntaxError: cannot assign to None
    $ return  # SyntaxError: 'return' outside function
  ```

> NameError:
  This occurs when a variable is not define, i.e. it has not been assigned yet

  ```bash
  # example
  $ test  # NAmeError : name 'test' is not define
  ```

> TypeError:
  An operation or function is applied to the wrong type
  python cannot interpret an operation on two data types

  ```bash
  # example
  $ len(5) # TypeError: object of type 'int' has no len()
  $  'awesome' + [] # TypeError: can only concatenate str (not "list") to str
  ```

> IndexError
  occurs when you try to access and element in a list an invalid index(i.e one that is outside the range of the list or string):

  ```bash
    # example
    $ list =['hello']
    $ list[2] # IndexError: list index out of range
  ```

> ValueError
  This occurs when a built-in operation or function receive as argument that has the right type but an inappropriate value:

  ```bash
  # example
  $ int('foo')  # ValueError: invalid literal for int() with base 10: 'foo'
  ```

> KeyError
  This occurs when a dictionary does not have a specific key:

  ```bash
  # example
  $ d = {}
  $ d ['foo']  # KeyError: 'foo'KeyError: 'foo'
  ```

> AttributeError
  This occurs when a variable does not have an attribute

  ```bash
  # example
  $  "awesome".foo  # AttributeError: 'str' object has no attribute 'foo'
  ```

## Raise Your own Exceptions

> in python we can also throw error using the raisekeyword. This is helpful when create your own kinds of exceptions and Error

  ```bash
  # eample
  $ raise ValueError('invalid value')
  $ raise NameError('invalid name')
  ```

## Handle Errors

> python, it is strongly encourage to use try/except blocks, to catch exceptions when we can do something about them. Let's see what that looks like

  ```bash
  # example 
  $ try:
  $  foobar
  $ except Namerror as err:
  $   print(err)
  ```

> else and finally part of of the Error handle

  ```bash
  # Example
  $ try:
  $    num = int(input("Please enter a number:  "))
  $ except ValueErro:
  $     print("this is not a number!")
  $ else:
  $    print("I'm in the ESLE")
  $ finally:
  $    print("Runs NO MATTER WHAT!")
  ```

>> the more usefull in loops  

  ```bash
  # example above
  $  while True:
  $      try:
  $          num = int(input("Please enter a number for the While:  "))
  $      except ValueError:
  $          print("this is not a number!")
  $      else:
  $          print("I'm in the ESLE")
  $          break
  $      finally:
  $          print("Runs NO MATTER WHAT!")
  $  print("REST OF GAME LOGIC RUS!")
  ```

> Debugging with pdp  [see here](/0x07_Debugging%20and%20Error%20Handling/pdb.py)
>> what is pdb : Python debugger  
>>> this is a modules to set breakpoint in our code we can use pdb by inserting this line

  ```bash
  # example
  $ import pdb; pd.set_trace
  ```
