# LAMBDA : IT IS A FUNCTION USE INSIDE A FUNCTION TO MAKE JOB EASY

> lambda is a built in function of it own
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
