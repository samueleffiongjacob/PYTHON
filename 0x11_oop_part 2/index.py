# Inheritance example
class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"This animal say {sound} ")


#  The class below inherite from Animal above
# Cat class inherits from Animal
class Cat(Animal):
    pass


# Make a new cat instance
gandalf = Cat()
# Because of inheritance, a Cat has access to:
gandalf.make_sound("meow")  # Meow
print(gandalf.cool)  # true

# gandalf is both a Cat and Animal (and base object)
# To verify if the instance works for all base object
print(isinstance(gandalf, object))

# to veriy if it works for just one
print(isinstance(gandalf, Cat))
