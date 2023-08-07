# Lambdas and Built-In Functions

> LAMBDA : IT IS A FUNCTION USE INSIDE A FUNCTION TO MAKE JOB EASY
>> lambda is a built in function of it own
>> when u call a lambda u are excuting a function but it that is as no name

```bash
# A regular named function
$ def square(num): return num * num

# An equivalent lambda, saved to a variable
$ def square2(num): return num * num

# Another lambda
$ def add(a, b): return a + b

# Executing the lambdas
$ print(square2(7))
$ print(add(3, 10))

# Notice that the square function has a name, but the two lambdas do not
$ print(square.__name__)
$ print(square2.__name__)
$ print(add.__name__)
```

## Maps with lambda

- a standard function that accepts at least two argurments, a function and an "iterable"
- iterable - something that can be iterated over (lists,strings,dictionaries, sets, tuples)
- run the lambda for each value in the iterable and returns a map object which can be converted into another data structure

Example on map

```bash
# maps example 
$ people = ["Samuel", "Effiong", "Dana"]
$ peeps = map(lambda name: name.upper(), people)  # always conver to a list
$ peepse = list(peeps)
$ print(peepse)

# check code for more
```

## filter

- there is a lambda for each value in the iterable
- Return filter object which can be converted into other iterables
- the object cointains only the values that return true to lambda
- for every expression filter puts it on a new list

```bash
# filter example
$ l = [1,2,3,4]
$ evens = list(filter(lambda x : x % 2 == 0, l))
$ print(evens) # [2,4]
```

> COMBING FILTER AND MAP
>> given  this list of names
>> `name = ["SAMUEL", "COLT", "RUSTY"]`
>> Return a new list with the string "YOUR instructor is" + each value in the array, but only if than 5 characters
>>
>> ```list(map(lambda name: f"your instructor is {name}",
>>      filter(lambda value: len(value) < 5, name)))```
>>> What about List Comprehension?
>> given  this list of names
>> `name = ["SAMUEL", "COLT", "RUSTY"]`
>> Return a new list with the string "YOUR instructor is" + each value in the array, but only if than 5 characters
>> [f"your instructor is {name}" for name in names if lens(name) < 5]
