# fist python function
def say_hi():
    print("hi!")


say_hi()

# Retuning Values From Function


def squre_of_7():
    return 7 ** 2


result = squre_of_7()

print(result)

from random import random
def flip_coin():
    # generate random number
    r = random()
    if r > 0.5:
         return "Heads"
    else:
        return "tails" 
value1 = flip_coin()
print(value1)