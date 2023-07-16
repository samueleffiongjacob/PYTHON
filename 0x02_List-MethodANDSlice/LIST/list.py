"""
    @list creation
    @ WHAT IS A LIST : a list is offten use to store varaible in a data
    set called it tempray data set. or it is a collection of grouping items
    @ACCESSING LIST
    @ Iterating Over Lists using loops
"""

# LIST creation

Name_list = ["SAM", "LINDA", "jerry", "moses", "favour"]
print(Name_list)  # SEEING EVERYTHING IN THE LIST

# # ACCESSING LIST
colt = range(1, 100)
me = 1 in colt
print(me)

tr = "SAMUEL" in Name_list
print(tr)

nam = Name_list[2]
print(nam)

# Iterating Over Lists using for loops
for linda in Name_list:
    print(linda)

# Iterating Over Lists using while loops
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
i = 0
while i < len(numbers):
    print(i)
    i += 1

# differnt way to write to get differnt output
while i < len(numbers):
    print(numbers[i])
    i += 1


# using f string to make it better
Name_lists = ["SAM", "LINDA", "jerry", "moses", "favour"]
index = 0
while index < len(Name_list):
    print(f"{index} : {Name_list[index]}")
    index += 1
