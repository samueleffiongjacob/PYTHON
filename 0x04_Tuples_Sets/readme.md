# Objectives

- Describe, create and acess tuples and sets
- Use built in method to modify set and acess values in tuples
- iterate over sets using loops and set comprehension
- compare and contrast set and tuple with list and dictionaries

## What is TUPLE: An ordered collection or grouping of items

```numbers = (1,2,3,4,5)```

Tuple is immutable : it can't not be change or order way of storing data

## Immutable: can never be change

```bash
$ x = (1,2,3)
$ v = 3 in x # True
x[0]='change me!' # TypeError: 'tuple' object does not support items assignment
```

## Why use a Tuple?

- tuple are faster than list
- it makes your code safer
- Valid Key in a dictionary

## Creating: using() or the tuple function

## Accessing tuple: accesing is just like a list

```bash
first_turple = (1,2,3,4,5,6)
first_turple[1] # 2
first_turple[-1] # 2

second_tuple = tuple(5,1,2)
second_tuple[0] # 5
second_tuple[-1] # 2
```

## looping/iletrating on tuple

```bash
$ months = ('January', 'February', 'March','April', 'May', 'June', 'July','August', 'September','October','November', 'December')

# using for loops
$ for month in months:
     print(month)

# using while
$ i = len(months) - 1
$ while i >= 0:
     print(f" \n {months[-i]}")
     i -= 1
```

## METHOD in tuples

- count
- index

Count: Returns the number of times a values appears in a tuple

```bash
# tuple count method
$ x = (1,2,3,3,3)
$ x.count(1) # 1
$ x x.count(3) # 3
```

index : Returns the index at which a value is in a tuple.

```bash
# tuple index method
x = (1,2,3,3,3)
x.count(1) # 1
x x.count(3) # 3
```

nested tuples

```bash
$ nums = (1,2,3,(4,5),6,7)
$ num[3]  # (4,5)

# get 5 from  index3
$ num[3][1] #5

# we use slices
$ nums[0:] #  (1,2,3,(4,5),6,7)

$ nums[0:4] #  (1,2,3,(4,5))

$ nums[0:4:2]  # (1,3) 
# kindly check my documentaion for slicing to understand what the above does
```

## SETS : this are collection of data that do not have duplicate value

- Sets are like formal mathemaatical sets.
- sets do not have duplicate values
- Element in sets aren't ordered
- you cannot access items in a set by index.
- set can be useful if you need to keep track of a collection of element , but don't care about ordering, keys or values and duplicates

## Creating / Acessing

```bash
# Set cannot have duplicate
$ s = set({1,2,3,4,5,5,5})  
# result of the above {1,2,3,4,5}

# Creating a new set 
$ s= set({1,4,5})

# can als be done as
$ s = {1,2,3} #note this different from dictionary.. check documention of dictionary above

$ in s # True

$ in S #False

```

## Acessing All values in a set using for loop

```bash
# looping through set

$ numbers = {1,2,3,4,5,56}

$ for more_nums in numbers:
          print(more_nums)

# good use case of set: assuming in a form we have more cities duplicate

$ cities = ["niger", "abuja", "cross", "niger", "abuja"]
# let clean up with set
$ new = set(cities)
$ print(new)

# you can covert a set back to list
$ print(list(set(cities)))

# we can just know the number of let in citys
$ print(len(set(cities)))
```

## Methods in Set

- add : adds element to a set. if the element is already in the set, the set doesn'r change:

```bash
# variable
$ man = set([1,2,3,4,5])

$ tt = man.add(6,7,8)
```

- remove : remove a value from the set - returns a KeyError if the value is not found

```bash
# variable
$ man1 = set([1,2,3,4,5])

$ tt1 = man1.remove(6,7,8)

# removing without keyError
$ tt2 = man1.discard(78)
```

- copy: creates a copy new sets.
- clear Removes all the contents in set
- Set Math : set have few other mathematical methods
 inclucding :
   intersection
   symmetric difference
   union

```bash
# variable
$ city = {"nigerAA", "abujSSa", "DDcross", "nSSiger" "aDDbuja"}
$ cityq = {"nigerAA", "abujSSa", "DDcross", "nSSiger","aDDbuja", "camerron", "port-harcout", "chelse"}

# union OF set
$ union = city | cityq
$ print(union)
# intersect of set
$ intersect = city | cityq
$ print(intersect)
```

## Set COMPREHENSION : this acutually similar to list, dictonary and tuple but there is a slight difference see below

```bash
# example
$ char = {x ** 2 for x in range(10)} # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# using string 
$ string = "hello"
$ string1 = "sequoia" # largest tree in the world
$ verify = len({char for char in string if char in "aeiou"})
$ verify1 = len({char for char in string1 if char in "aeiou"})
```
