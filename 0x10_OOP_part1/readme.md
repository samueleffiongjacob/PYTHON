# OBJECT ORIENTED PROGRAMMING (OOP)

## OBJECTIVES

- Define what Object Oriented Programming is?
- Understand encapsulation and abstraction
- Create classes and instances and attach methods and properties to each

### What is oop?

- object oriented programming is a method of programming that attempts to model some process or thing in the world as **class** or **object**.
- **class** : a blueprint for objects. Classes can contain methods (functions) and attribute (similar to keys in a dict).
**Instance** : Objects that are constructed from a class blueprint that contain their class's methods and properties.

> #### Why OOP?

- With Object oriented progarmming, the goals to encapsulate your code into **Logical, hierarchical groupings using classes** so that you can reason about your at a higer level.
![smauleffiongoopimage](/image/samue%20effiong%20oop%20image.png)

> **Example**
>> ![SAMUEL OOP EXAMPLE](/image/SAMUELEFFIONG%20OOP%20EXAMPLE.png)    ![SAMUELEFFIONG OOP EXAMPLE1](/image/SAMUELEFFIONG%20OOP%20EXAMPLE1.png)

## Encapsulation

- **Encapsulation** : the grouping of public and private attribute and method into a programmatic class, making **Abstraction** possible

>>>> *Example*

- Designing the Deck Class, I make **cards** a private attribute(a list)
- I decide that the lenght of the cards should be accessed via a pulic method **count()** -- i.e **Deck.count()**

## ABTRACTION

- **Abstraction** : exposing only `relevant` data in a class interface, hiding private atrribute and method(aka the "inner working") from users

```bash
# Creating a Class

$ class Vehicle:
$       def__init__(self, make,model,year):
$           self.make = make
$           self.mode = model
$           self.year = year
```

classes in python can have a special __init__method, which gets called every time you create an instance of the class(instantiate)

**Note** every time : There are some special cases. You might define a claa that only holds methods and no data.
`You wouldn't need an __init__ method in that case (rare!)`

The **self** Keywords refers to the specific instance of the User class or whatever we're working with.

## Class Attributes

- we can define class attribute directly on a class that are shared by all instances of a class and the class itself

>>> example Image
>>> ![SAMUEL EFFIONG CLASS METHOD EXAMLE](/image/class%20atribute_method.png)

## Class Methods

class Method are methods (with the @classmethod decorator) that are not concerned with instance, but the class itself.

```bash
# Class Methods Example
$ class Person():
$   ""class method""
$
$   @classmethod
$   def from_csv(cls,filename)
$       return cls(*params) # this is the sam as calling Person(*Params)
$ person.from_csv(my_csv)
```

## String Representation

> The __repr__method is one of serveral ways to provide a nicer string representation

```bash
# example
$ class Human:
$   def__init__(self,name="someone"):
$       self.name = name
$   def__repr__(self):
$       return self.name
$ dude = Human()
$ print(dude) # "somebody"
$ colt = Human(name="Samuel Effiong")
$ print(f"{Samuel} is totally rad (probably)")
```
