# age = 21

age = input("ENTER YOUR AGE TO DETERMINE TASK \n")

if age != "":
    if not ((int(age) >= 2 and int(age) <= 8) or int(age) >= 68):
        print(
            f"YOUR AGE BRACKET {age} you are not a child or senior please pay in dollars")
    else:
        print(f"u are a child aged {age} pay no dollars")

else:
    print(f"{age} is not a number, please enter a number eg : 1-900")
