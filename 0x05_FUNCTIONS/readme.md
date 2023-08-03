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

## CREATING A FUNCTION that accept input

```bash
# function accept only one parameter
$ def squre(num): 
    return num * num
$ print(square(4))
$ print(square(8))

# fun that accept two parameters
$ def add(a,b):
    return a+b

# example 2 for for accepting two parameter
$ def multipy(ket, man):
    return ket * man

$ multipy (5,5) #25
$ add (5,5) # 10

# Naming parameter 
$ def print_full_name(first_name, last_name):
    return(f"your full name is : \n {first_name}  {last_name}")

wed = print_full_name("SAMUEL EFFIONG", "JACOB")
print(wed)
```

## Parameters vs Arguments

- A parameter is a variable in a method defination
- When a method is , the arguments are the data you pass into the method's  Parameters
- Argument is the actual value of this variable that get passed to function

## Default parameter

```bash
$ def exponent(num, power=2):
     return num ** power
$ print(exponent(2, 3))  # 8
$ print(exponent(3))  # 9
```

## Why have Default Params?

- Allows you to have defensive
- Avoids error with incorrect parameters
- more readable example

## What Can Default Parameters Be?

- Anything! function, list ,dictionaries, strings, boolean - all of the above

## Keyword argurment

- unpacking a function.
- allow u to change params
- it does not change arguemet

## Document Functions

- Use """ """
- Essential when writing complex functions

```bash
# document string example
$ def say_hello():
$    """ A simple function that returns the string hello """
$   return "hello"

# Accesing document of any function using .__doc__
$ say_hello.__doc__ # A simple function that returns the string 
```
