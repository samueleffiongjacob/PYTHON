# DeFINING THE SIMPLEST POSSIBLE CLASS

class User1:
    pass


user1 = User1()
print(type(user1))


# Creating a new user __init__(self) we would talk more on self later

class User2:
    def __init__(self):
        print("A NEW USER AS BEEN CREATED!")


user2 = User2()
user3 = User2()
user4 = User2()


# Making resable real life code

class User:
    def __init__(self, first, last, age):
        """self is a specific instance in a class.
        A User class with 3 attributes but no methods (aside from __init__)
        """
        self.first = first
        self.last = last
        self.age = age


user5 = User("joe", "sma", 64)
user6 = User("sam", "sma", 64)

# To access specific attribute on an instance, we run
# instance.attribute_name

print(user5.first, user5.last, user5.age)
print(user6.last)
