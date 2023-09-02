# Raising your error
""" how to raise error 
raise __
types of error:
    1.TypeError
    2.ValueError
    3.NameError
"""
def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")


colorize('cyan', "blue")  # correct format
# colorize(34, "red")  # wrong

# Handle Errors
try:
    foobar
except NameError:
    print("\n PROBLEM")
print("after the try")


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


d = {"name": "Ricky"}
print(get(d, "name"))

# else and finally part of of the Error handle
try:
    num = int(input("Please enter a number:  "))
except ValueError:
    print("this is not a number!")
else:
    print("I'm in the ESLE")
finally:
    print("Runs NO MATTER WHAT!")

# the above is commonly use in a loop

while True:
    try:
        num = int(input("Please enter a number for the While:  "))
    except ValueError:
        print("this is not a number!")
    else:
        print("I'm in the ESLE")
        break
    finally:
        print("Runs NO MATTER WHAT!")
print("REST OF GAME LOGIC RUS!")


# More advance example
def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("don't divide by zero please!")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

# More clean:


def divide(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong!")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")


print(divide(1, 2))
print(divide(1, 'a'))
print(divide(1, 0))
