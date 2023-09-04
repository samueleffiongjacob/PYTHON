# OBJECT ORIENTED PROGRAMING PART 2

> OBJECTIVE

- implementation inheritance, including multiple
- Understand Method Resolution Order
- Understand polymorphism
- add special method to classes

## Inheritance

A key feature of OOP is the ability to define a class which inherits from another class (a "base" or "parent" class).

in python, inheritance works by passing the parent class as an argument to the definition of a child class

```bash
# Inheritance example 
$ class Animal: 
$   def make_sound(self, sound):
$       print(sound)
$   cool = True
$
$
#  The class below inherite from Animal above
$ class Cat(Animal):
$   pass
$ gandalf = Cat()
$ gandalf.make_sound("meow")  # Meow
$ gandalf.cool # true
```

### @property, @age.setter, super().__init__(name, species="Cat")

the above make job easier

### multiple inheritance

this just a way to call mutiple class
![samuel effiong multiple inheritance](/image/multiple.png)     ![samuel effiong multiple inheritance 2](/image/mutiple2.png)

### Method Resolution Order (MRO)

whenever you create a class, python set a Method Resolution Order, Or MRO, for that class, which is the order in which python will look methods on instance of that class.

> You can programmatically reference the MRO three ways:

- __mro__attribute on the class
- use the mro()method on the class
- use the builtin help(cls)method

![exaple samuel effiong mro](/image/mro.png)

## Polymorphism

![POLYMORPHISM SAMUEL](/image/polymorphism.png)   ![POLYMORPHISM SAMUEL1](/image/polymorphism1.png)

- Special Methods

> (polymorphism) The same operation works for different kinds of Objects
>> How does the following work in python?
![SPECIAL DUNDER](/image/samule%20speacial.png)
