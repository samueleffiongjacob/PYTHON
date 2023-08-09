# max example
import math as maths

me = max(3, 4, 5, 100)  # 100
# min example
me1 = min(3, 4, 5, 100)  # 3
print(me, me1)

names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
me2 = min(len(name) for name in names)  # 3
print(me2)
# find the longest name itself
me3 = max(names, key=lambda n: len(n))  # Ollivander
print(me3)

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
# {"title": "happy birthday", "playcount": 1}
me4 = min(songs, key=lambda s: s['playcount'])
print(me4)
# Finds the title of the most played song
me5 = max(songs, key=lambda s: s['playcount'])['title']  # YMCA
print(me5)

# recreate above
max = 0
for song in songs:
    if song['playcount'] > max:
        max = song["playcount"]
print(max)

# REVERSED
nuns = [1, 2, 3, 4]
num1 = list(reversed(nuns))
print(num1)

# for string
for char in reversed("hello world"):
    print(char)

# slice method previously
math = "hello"
math1 = math[::-1]
print(math1)

for x in reversed(range(1, 10)):
    print(x)

en = len("hello")
print(en)

en2 = 'hello'.__len__()
print(f"new lenght on string method : \n {en2}")

# Introducing class length


class Speciallist:
    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return 50


li = Speciallist([1, 2, 3, 4, 200, 30])
l2 = Speciallist([])

# this gives length divided by 2


class Speciallist2:
    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return self.__data.__len__() // 2


li = Speciallist2([1, 2, 3, 4, 200, 30])
l2 = Speciallist2([])

print(len(li))
print(len(l2))

# ABS
abs1 = abs(3.4444)  # 3.4444

abss = abs(-3.444)  # 3.444

print(abs1, abss)

# abs to covert strings into float value
pyt = abs(float('20'))

# method fabs in python
pytw = maths.fabs(-4)
print(pyt, pytw)

# Sum
# example of sum using list, tuples, and set

# list
sum1 = sum([1, 2, 3])  # 6

# tuples
sum12 = sum((1, 2, 3))  # 6

# set
sum13 = sum({1, 50, 100})  # 151

# u can pass in an extra parameter. but it would start
#  calculation from that parameter

sum2 = sum([1, 2, 3], 10)  # 16

# tuples
sum21 = sum((1, 2, 3), -6)  # 0

# set
sum22 = sum({1, 50, 100}, -50)  # 101

print(f" first sum : \n {sum1} \n {sum12} \n {sum13}")
print(f" second sum : \n {sum2} \n {sum21} \n {sum22}")

# Round
# example
ron = round(10.2)  # 10

# when specified how digit should be rounded
ron1 = round(1.212121, 2)  # 1.21

# if pass in value 'none' it would to the nearest interger
ron12 = round(1.212121, None)  # 1

print(f"round: \n {ron} \n {ron1} \n {ron12}")

# ZIP
# zip example
first_zip = zip([1, 2, 3], [4, 5, 6])
words = ['hi', 'lol', 'haha', ':)']
zer = zip([1, 2, 3], [4, 5, 6])
zer1 = zip([1, 2, 3], [4, 5, 6])
first_zip0 = list(first_zip)  # [(1, 4), (2, 5), (3, 6)]
first_zip1 = dict(zer)  # {1: 4, 2: 5, 3: 6}
# [('hi', (1, 4)), ('lol', (2, 5)), ('haha', (3, 6))]
first_zip2 = list(zip(words, zer1))

# using args to upack list into zip
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
first_zip3 = list(zip(*five_by_two))  # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

print(f"{first_zip0}, {first_zip1}, \n {first_zip2} \n {first_zip3}")


