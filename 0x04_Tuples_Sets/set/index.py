# Starting up sets
# to print any of the below use ```print(variable)```
# Set cannot have duplicate

s = set({1, 2, 3, 4, 5, 5, 5})  # {1,2,3,4,5}

# Creating a new set
q = set({1, 4, 5})
print(q)

# can als be done as
# note this different from dictionary.. check documention of dictionary above
d = {1, 2, 3}
print(d)

e = 4 in s  # True
print(e)

v = 8 in s  # False
print(v)

# Acessing All values in a set using for loop


# looping through set

numbers = {1, 2, 3, 4, 5, 56}

for more_nums in numbers:
    print(more_nums)

# good use case of set: assuming in a form we have more cities duplicate

cities = ["niger", "abuja", "cross", "niger", "abuja"]
# let clean up with set
new = set(cities)
print(new)

# you can covert a set back to list
print(list(set(cities)))

# we can just know the number of let in citys
print(len(set(cities)))

# methods in set

city = {"nigerAA", "abujSSa", "DDcross", "nSSiger", "aDDbuja"}
cityq = {"nigerAA", "abujSSa", "DDcross", "nSSiger",
         "aDDbuja", "camerron", "port-harcout", "chelse"}

# union OF set
union = city | cityq
print(union)
# intersect of set
intersect = city | cityq
print(intersect)

# Set COMPREHENSION : this acutually similar to list, dictonary
#  and tuple but there is a slight difference see below example
char = {x ** 2 for x in range(10)}  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(char)
# using string
string = "hello"
string1 = "sequoia"  # largest tree in the world
verify = len({char for char in string if char in "aeiou"})
verify1 = len({char for char in string1 if char in "aeiou"})

verify2 = len({char for char in string if char in "aeiou"}) == 5
verify3 = len({char for char in string1 if char in "aeiou"}) == 5
print(f"value that  contain all vowel:\n {verify}")
print(f"value that  contain all vowel:\n {verify1}")
print(f"value that  contain all vowel in bolean:\n {verify2}")
print(f"value that  contain all vowel in bolean:\n {verify3}")
