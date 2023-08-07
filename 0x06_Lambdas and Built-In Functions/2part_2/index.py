# max example
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
