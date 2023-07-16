"""
    excerice in loops
"""
# just once
for num in range(1, 11):
    print("\U0001f600" * num)

"""
    @nested loop
     for loop that repeat a work 3 times or any numbers
"""
for x in range(3):
    for num in range(1, 11):
        print("\U0001f600" * num)

# for while loop

time = 1
while time < 11:
    print("\U0001f600" * time)
    time += 1

# Without string multiplication - ugly solution

for num in range(1, 11):
    count = 1
    smileys = ""
    while count <= num:
        smileys += "\U0001f600"
        count += 1
    print(smileys)

# center pyramid
time = 1
while time < 11:
    print("      \U0001f600" * time)
    time += 1
