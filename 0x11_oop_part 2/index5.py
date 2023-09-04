class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is Swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"


class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is Walking"

    def greet(self):
        return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        super().__init__(name=name)
        """
        To be more explicity about what you want
        to use below that is commented out
        kindly comment super class and uncomment below
        """
        # Ambulatory.__init__(self, name= name)
        # Aquatic.__init__(self, name=name)


jaws = Aquatic("jaw")
lassie = Ambulatory("SAMUEL EFFIONG")
captain_cook = Penguin('captian cook')
print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())


print(
    f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(
    f"captain_cook is instance of Penguin: {isinstance(captain_cook, Aquatic)}")
print(
    f"captain_cook is instance of Penguin: {isinstance(captain_cook, Ambulatory)}")
