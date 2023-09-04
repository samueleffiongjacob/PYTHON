class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    # NEW CODE

    def __repr__(self):
        return f"{self.first} is {self.age}"
    # NEW CODE

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"


class moderator(User):
    # check the number of moderator
    total_mod = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        moderator.total_mod += 1

    @classmethod
    def display_active_mod(cls):
        return f"There are currently {cls.total_mod} active moderators"
    
    def remove_post(self):
        return f"{self.full_name()} remove a post from the {self.community} community"


tom = moderator("Jassam", "0'conner", 61, "piano")

#j = str(j)
print(tom.full_name())
print(tom.community)


# second example:
print(User.display_active_users())
j = User("judy", "steele", 18)
print(User.display_active_users())
tom = moderator("Jassam", "0'conner", 61, "piano")
print(User.display_active_users())


# third example
j1 = User("judy", "steele", 18)
j2 = User("judy", "steele", 18)
j3 = User("judy", "steele", 18)
tom1 = moderator("Jassam", "0'conner", 61, "piano")
tom2 = moderator("Jassam", "0'conner", 61, "piano")
print(User.display_active_users())
print(moderator.display_active_mod())