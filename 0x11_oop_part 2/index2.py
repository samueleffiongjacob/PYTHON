# Properties
class Human1:
    def __init__(self, first, last, age):
        self.firt = first
        self.last = last
        # checking and vering age.. Don't use self.age her for it to work
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            self._age = 0


jane = Human1("jane", "Godwill", -9)
print(jane.get_age())
jane.set_age(45)
print(jane.get_age())

# Now Using the property methods


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # instead of doing the get age and set age above
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age must not be negative")

    @property
    def full_name(self):
        return f"{self.first}, {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")


jane = Human("jane", "Godwill", -9)
print(jane.age)
# jane.age = -30
jane.age = 20
print(jane.age)
print(jane.full_name)
jane.full_name = "SAMUEL EFFIONG"
print(jane.__dict__)
