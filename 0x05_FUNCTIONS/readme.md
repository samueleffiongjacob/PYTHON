# Objectives

- describe what a function is and how they are useful
- Explain exactly what the return keyword does and some of the side effect when using it
- Add parameters to function to output different data
- Define and diagram how scope works in a function
- Add Keywords arguments to functions

## What are functions

- it is process of excuting task
- it can accept input and return output
- Useful for excuting similar procedures over and over

## Why use Functions?

- Stay Dry - Don't Repeat Yourself!
- clean up and prevent code duplication
- "Abstraction away" code for others user

## Function Structure

```bash
# function block
$ def name_of_function ():
    #block of code

# example
$ def say_hi():
    print("Hi!")
$ say_hi()
```

## Retuning Values From Function

```bash
# returning function created
$ def squre_of_7():
    return 7 ** 2
$ result = squre_of_7()
$ print(result)
```

## return

- Exit the function
- Outputs whenever values is place after the return keyword
- pops the function off the call stack
