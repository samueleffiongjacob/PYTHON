# fist python function
from random import random


def say_hi():
    print("hi!")


say_hi()

# Retuning Values From Function


def squre_of_7():
    return 7 ** 2


result = squre_of_7()

print(result)


def flip_coin():
    # generate random number
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "tails"


value1 = flip_coin()
print(value1)

# CREATING A FUNCTION that accept input

# function


def squre(num):    # accept only one parameter
    return num * num


print(squre(5))
print(squre(3))


def happy_birth(name):
    print(f"happy_birth {name}")


print(happy_birth("samuel"))

# CREATING A FUNCTION that accept input


# function accept only one parameter
def squre(num):
    return num * num


print(squre(4))
print(squre(8))

# fun that accept two parameters


def add(a, b):
    return a+b

# example 2 for for accepting two parameter


def multipy(ket, man):
    return ket * man


multipy = multipy(5, 5)  # 25
add = add(5, 5)  # 10
print(add)
print(multipy)

# Naming parameter


def print_full_name(first_name, last_name):
    return (f"your full name is : \n {first_name}  {last_name}")


wed = print_full_name("SAMUEL EFFIONG", "JACOB")
print(wed)

# COMMON MISTAKE PEOPLE MAKE IN FUNCTION
# OLD-VERSION----OLD-VERSION----OLD-VERSION-----


def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total  # Returning too early :(
# OLD-VERSION----OLD-VERSION----OLD-VERSION-----


# NEW AND IMPROVED VERSION :)
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total


print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))

# exam 2

# OLD=VERSION===OLD=VERSION===OLD=VERSION


def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:  # This else is unnecessary
        return False
# OLD=VERSION===OLD=VERSION===OLD=VERSION


def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False  # We can just return without the else


print(is_odd_number(4))
print(is_odd_number(9))

# Default parameter


def exponent(num, power=2):
    return num ** power


print(exponent(2, 3))  # 8
print(exponent(3))  # 9
print(exponent(7))  # 49


def add(a, b):
    return a+b


def math(a, b, fn=add):
    return fn(a, b)


def subtract(a, b):
    return a-b


print(math(4, 5))  # results in add(4,5) which is 9

print(math(4, 5, subtract))  # results in subtract(4,5) which is -1

# EXAMPLE OF A SCOPING PROBLEM:
total = 0


def increment():
    total += 1
    return total

# to run the below remove the #
# print(increment())  # Error!

# "I can't find a variable named total in this function"


total = 0


def increment():
    global total  # use the global variable total
    total += 1
    return total


print(increment())  # 1
print(increment())  # 2
print(increment())  # 3

# Document Functions

# document string example


def say_hello():
    """ A simple function that returns the string hello """
    return "hello!"


# Accesing document of any function using .__doc__
print(say_hello.__doc__)  # A simple function that returns the string

# example 2


def exponent(num, power=2):
    """exponent(num, power)raises num to specified power.
    Power defaults to 2."""
    return num ** power


print(exponent(2, 3))  # 8
print(exponent(3))  # 9
print(exponent(7))  # 49

print(exponent.__doc__)
