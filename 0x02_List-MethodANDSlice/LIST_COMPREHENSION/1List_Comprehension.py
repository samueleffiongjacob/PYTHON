"""
    @List Comprehension
    syntax : [__for __in __]
"""
nums = [1, 2, 3, 4, 5]
num1 = [x*10 for x in nums]

num2 = [x/2 for x in nums]
print(num2, num1)

# LIST COMPRESION VERSE for loop
num3 = []
for num4 in nums:
    num5 = num4 * 2
    num3.append(num5)
print(f"This are the new values of num3 using for loop: {num3}")
# vs list comprehension
numbers = [num6 * 2 for num6 in nums]
print(f"This are the new values of num6 using list comprehension: {numbers}")


# list comprehension for string
name = "samuel"
names = [char.upper() for char in name]
print(f"Char list in names : {names}")

# how to take first character and uppercase
friends = ['samuel', 'moses', 'grace', 'haser']
saw = [my[0].upper() for my in friends]
print(saw)

sew = [num*10 for num in range(1, 6)]  # looping throug range
sew1 = [bool(val)for val in [0, [], '']]  # checking trutiness
print(sew, sew1)


# converting numbers to string
string = [str(seed) for seed in nums]
print(string)

# let add a string to it
string1 = [str(seed) + "hello" for seed in nums]
print(string1)
