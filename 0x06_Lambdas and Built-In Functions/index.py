# A regular named function
# import tkinter as tk
import sys
def square(num): return num * num


# An equivalent lambda, saved to a variable
def square2(num): return num * num


# Another lambda
def add(a, b): return a + b


# Executing the lambdas
print(square2(7))
print(add(3, 10))

# Notice that the square function has a name, but the two lambdas do not
print(square.__name__)
print(square2.__name__)
print(add.__name__)


# example 2 on lambda
# root = tk.Tk()  # creaating environment for running
# frame = tk.Frame(root)  # creating frame
# frame.pack()  # creating a block for the design

# # Don't need this function if we use a lambda
# # def say_hi():
# #     print("HELLO!")

# button = tk.Button(frame, text="CLICK ME", fg="green",
#                    command=lambda: print("SAMUEL IS GOOD "))
# button.pack(side=tk.RIGHT)
# root.mainloop()

# maps
numbs = [3, 5, 7, 9, 11]
# to view it must be use with list or others ways
double = map(lambda x: x * 2, numbs)
double1 = list(map(lambda x: x*2, numbs))  # note it can be use once
print(double1)

num = [2, 4, 6, 8, 10]
num_mutiple = map(lambda x: x*2, num)
for num in num_mutiple:
    print(num)

people = ["Samuel", "Effiong", "Dana"]
peeps = map(lambda name: name.upper(), people)  # always conver to a list
peepse = list(peeps)
print(peepse)

Name = [
    {"first": "samuel", "last": "effiong"},
    {"first": "samuel", "last": "effiong"},
    {"first": "samuel", "last": "effiong"}
]

names = list(map(lambda x: x["first"], Name))
print(names)

# or by using function in maps.. but the pain is u have
# to define function for every maps
double_me2 = [2, 4, 6, 8, 10]


def double_me(x): return x * 2


double_me1 = list(map(double_me, double_me2))
print(double_me1)

# ## filter

# filter example
la = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, la))
print(evens)  # [2,4]

# example 2
a_name = ['austin', 'penny', 'anthony', 'angel', 'billy']
name = list(filter(lambda n: n[0] == 'a', a_name))
print(name)

# example 3
users = [
    {"username": "samuel", "tweets": [
        "I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

# using filters with lambda

# extract inactive users using filter:
inactive = list(filter(lambda u: len(u['tweets']) == 0, users))
print(inactive)

# taking advantage of knowing that an empty list false to extract active user
active = list(filter(lambda u: u['tweets'], users))
print(active)  # this fetch tweet

# taking advantage of knowing that an empty list false
#  to extract inactive users
inactive_u = list(filter(lambda u: not u['tweets'], users))
print(inactive_u)

# extract inactive users using list comprehension:
inactive_user2 = [user for user in users if not user['tweets']]
print(inactive_user2)
# using maps and fillters to select inactive users and username

username = list(map(lambda user: user["username"].upper(),
                    filter(lambda u: not u['tweets'], users)))
print(username)

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]
print(username)

# all
mee4 = all([0, 1, 2, 3])  # false
mee3 = all([char for char in 'eio' if char in 'aeiou'])
mee = all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])  # false

print(mee, mee3, mee4)

# any
mw = any([0, 1, 2, 3])  # false```
mw1 = any([char for char in 'eio' if char in 'aeiou'])
mw2 = any([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])  # false
mw3 = any([val for val in [1, 2, 3] if val > 2])  # True
mw4 = any([val for val in [1, 2, 3] if val > 5])  # Fasle
print(mw, mw1, mw2, mw3, mw4)

# genarator expression
# A simple comparison of size (in Bytes)
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")
