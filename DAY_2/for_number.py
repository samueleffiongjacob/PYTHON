"""
    @for loop to operate state on range in python
"""

for count in range(1, 21):
    if count == 4 or count == 13:
        print(f"{count} is unlucky")
    elif count % 2 == 0:
        print(f"{count} is even")
    else:
        print(f"{count} is odd")

# Slight Refactor
for count in range(1, 21):
    if count == 4 or count == 13:
        states = "unlucky"
    elif count % 2 == 0:
        states = "even"
    else:
        states = "odd"
    print(f"{count} is {states}")
