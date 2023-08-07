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
   `name = ["SAMUEL", "COLT", "RUSTY"]`  
>> Return a new list with the string "YOUR instructor is" + each value in the array, but only if than 5 characters
>>>
```bash
# see example
$ list(map(lambda name: f"your instructor is {name},
$       filter(lambda value: len(value) < 5, name)))
```

> What about List Comprehension?
>> given  this list of names.  
   ```name = ["SAMUEL", "COLT", "RUSTY"]```  
>> Return a new list with the string "YOUR instructor is" + each value in the array, but only if than 5 characters
>>>
```bash
[f"your instructor is {name}" for name in names if lens(name) < 5]
```

## All

>> Return True if all elements of the iterable are truthy (or if the iterable is empty)

```bash
all([0,1,2,3]) #false
all([char for char in 'eio' if char in 'aeiou'])```
all([num for num in [4,2,10,6,8] if num % 2 == 0]) # false
```

## ANy

>> Return True if any elements of the iterable are truthy. if the iterable is empty, return False

``` bash
# example
$ any([0,1,2,3]) #false
$ any([char for char in 'eio' if char in 'aeiou'])
$ any([num for num in [4,2,10,6,8] if num % 2 == 0]) # false
$ any([val for val in [1,2,3] if val > 2]) # True
$ any([val for val in [1,2,3] if val > 5]) # Fasle
```

## genarator expression

> Basically use a genarator expression, if all your're doing is iterating once. if you want to store and use the generated results, then you're probably better of list comprehension

## Sorted

>> Returns a new sorted list from the items in iterabls

```bash
# Sorted (works on anything that is iterable)
$ more_number = [6,1,8,2]
$ sorted(more_number) # [1,2,6,8]
$ print(more_number)  # [6,1,8,2]
```
