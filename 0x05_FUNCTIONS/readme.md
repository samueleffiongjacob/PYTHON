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

## FUNCTION PART TWO

  OBJECTIVES 1
    - Use the * and ** operator as parameters to a function and outside of a function
    - Leverage dictionary and tuple unpacking to create more flexible function
    The above are often call `*args`
    - A special operator we can pass to function
    - Gather remaining argument as a **tuple**
    - **This is just a parameter** - you can call it whatever you want
    The above are often `**kwargs`
    - This a special operation we can pass to functions
    - Gathers remaining keyword argument as a **dictionary**
    -  **This is just a parameter** - you can call it whatever you want
**Example below**

```bash
# Starting out function 2
    $ def correct_info(*args):
        if "Samuel" in args and "effiong" in args:
            return "WELCOME BACK EFFIONG !"
        return "NOT SURE WHO YOU ARE"
    print(correct_info("heloo", False, 78))  # "NOT SURE WHO YOU ARE"
    print(correct_info("Samuel", True, 1, "effiong"))  # "WELCOME BACK EFFIONG !"

    def sum_all_numbers(*nums):
    total = 0
    for num in nums:
        total += num
    return total
    print(sum_all_numbers(75, 56, 5, 64, 3, 245, 35, 3))
    print(sum_all_numbers(4, 6))

```

```bash
# **kwargs
$ def special_greeting(**kwargs):
        if "David" in kwargs and kwargs["David"] == "special":
            return "You get a special greeting David!"
        elif "David" in kwargs:
            return f"{kwargs['David']} David"
        return "not sure who u are"

    print(special_greeting(Heather="hello", David="special"))
    print(special_greeting(David='Hello'))  # Hello David!
    print(special_greeting(Bob='hello'))  # Not sure who this is...
    print(special_greeting(David='special'))  # You get a special greeting David!

# Example 2
$ def fav_colors(**Kwargs):
    for person, colors in Kwargs.items():
        print(f"{person}'s favorite color is {colors}")
    fav_colors(colt="purple", ruby="red", ethel="teal")
    fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")
    fav_colors(colt="royal deep amazing purple")
```

## FUNCTION PART  II

**Parameter Ordering**
    - parameters
    - *args
    - default parameters
    - ** kwargs

Example for Paremeter ordering

```bash
$ def display_info(a, b, *args, instructor="Colt", **kwargs):
  # return [a, b, args, instructor, kwargs]
  print(type(args))

    print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))

    # a - 1
    # b - 2
    # args (3)
    # instructor - "Colt"
    # kwargs - {'last_name': "Steele", "job": "Instructor"}

    [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]
```

> Using *as an Argument: Argument Unpacking
>> we can use* as an argument to a function to "unpack" values

```bash
# tuples unpacking
$ def unpack(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)
    nums = [1, 2, 3, 4, 5, 6,]  # to unpack this values use *
    unpack(*nums)
```

> Using **as an Argument: Argument Unpacking
>> we can use** as an argument to a function to "unpack" values

```bash
# dictionary unpacking
$ def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)


    data = dict(a=1, b=2, c=3, d=55, name="Tony")

    add_and_multiply_numbers(**data)  # 7
    add_and_multiply_numbers(**data, sam="green")  # 8
```
