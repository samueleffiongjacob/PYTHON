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