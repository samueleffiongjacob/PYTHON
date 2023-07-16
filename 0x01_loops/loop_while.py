"""
    @while loop
     Continues to ask for user input until the user types 'SAMUEL'
"""

msg = input("whats the secret password? \n")
while msg != "SAMUEL":
    print("WRONG!")
    msg = input("whats the secret password? \n")
print("CORRECT!")


num = 1
while num < 10:
    num += 1
    print(f"{num} is usually fine")
