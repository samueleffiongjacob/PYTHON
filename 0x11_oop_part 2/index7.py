class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")
        # note it is only when u are on team and u want to explitly define something


class Dog(Animal):
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"


class Fish(Animal):
    pass


d = Dog()
print(d.speak())
f = Fish()
print(f.speak())
