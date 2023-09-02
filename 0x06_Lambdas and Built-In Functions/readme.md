# Lambdas and Built-In Functions [part 1](/0x06_Lambdas%20and%20Built-In%20Functions/1PART_1/)

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
$ peeps = map(lambda name: name.upper(), people)  # always convert to a list
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
all([char for char in 'eio' if char in 'aeiou'])
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

## Lambdas and Built-In Functions [part 2](/0x06_Lambdas%20and%20Built-In%20Functions/2part_2/)

> Max : return the longest or largest item in an iterable or the largest of two or more arguments  
```max (3,4,5,100)```  
> Min : return the least or smallest item in an iterable or the largest of two or more arguments  
```min(3,4,5,100)```
> Reversed : Return a reverse *iterator*  

```bash
# example
$ nuns = [1,2,3,4]
$ list(reversed(nuns))
```

> Len : Return the length(the number of items) of an object. The argument may be a sequence (such as a string, tuple, list, or range) or a collection (such as a dictionary, set)  
>> ```'hello'.__len__()```
> Abs : Return the absolute value of a number. The argurmrnt may be interger or a floating point number.  

```bash
# abs usage
$ abs(3.4444) # 3.4444

$ abs(-3.444) # 3.444
```

>> using abs to covert strings into float value  
>> There is another method in python call fabs in python use for maths function.. fabs it take a value and convert it to float first see how it works below:  

```bash
# abs to covert strings into float value 
$ abs(float('20')) # 20.0

# method fabs in python
$ import maths
$ maths.fabs(-4) # 4.0
```

> Sum  
>> takes an iterable and an optional start  
>> Return the sum of start and items of an iterable from left to right and return the total  
>> start defaults  

```bash
# example of sum using list, tuples, and set

#list
$ sum([1,2,3])  #6

# tuples
$ sum((1,2,3))  #6

# set
$ sum({1,50,100})  #151

# u can pass in an extra parameter. but it would start calculation from that parameter

$ sum([1,2,3],10)  #16

# tuples
$ sum((1,2,3), -6)  #0

# set
$ sum({1,50,100}, -50)  #101
```

> Round : Return number rounded to ndigits precision after the decimal point. if ndigits is ommitted or is None, it returns the nearest integer to its input  

```bash
# example 
$ round(10.2) # 10

# when specified how digit should be rounded
$ round(1.212121, 2) #1.21

# if pass in value 'none' it would to the nearest interger
$ round(1.212121, None)  #1
```

> Zip  
>> Makes an iterator that aggregates element from each of the iterables.
>> Return an iterator of tuples, where the i-th tuples contain the i-th element from each of the argument sequence or iterable  
> The iterator stops when the shortest input iterable is exhausted  

```bash
# zip example
$ first_zip = zip([1,2,3], [4,5,6])
$ list(first_zip) #  [(1, 4), (2, 5), (3, 6)]
$ dict(first_zip) # {1: 4, 2: 5, 3: 6}
$ words = ['hi', 'lol', 'haha', ':)']
$ list(zip(words,first_zip)) # [('hi', (1, 4)), ('lol', (2, 5)), ('haha', (3, 6))]

# using args to upack list into zip
$ five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
$ list(zip(*five_by_two)) # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
```
