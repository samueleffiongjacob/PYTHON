# Starting out function 2
# * args
def correct_info(*args):
    if "Samuel" in args and "effiong" in args:
        return "WELCOME BACK EFFIONG !"
    return "NOT SURE WHO YOU ARE"


print(correct_info("heloo", False, 78))  # "NOT SURE WHO YOU ARE"
print(correct_info("Samuel", True, 1, "effiong"))  # "WELCOME BACK EFFIONG !"


def sum_all_numbers(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all_numbers(75, 56, 5, 64, 3, 245, 35, 3))
print(sum_all_numbers(4, 6))


def feed_me(*stuff):
    for thing in stuff:
        print(f"YUMMY I EAT {thing}")


feed_me("apple", "tire", "shoe", "salmon")

# **kwargs


def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David"
    return "not sure who u are"


print(special_greeting(Heather="hello", David="special"))

print(special_greeting(David='Hello'))  # Hello David!
print(special_greeting(Bob='hello'))  # Not sure who this is...
print(special_greeting(David='special'))  # You get a special greeting David!


def fav_colors(**Kwargs):
    for person, colors in Kwargs.items():
        print(f"{person}'s favorite color is {colors}")


fav_colors(colt="purple", ruby="red", ethel="teal")
fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")
fav_colors(colt="royal deep amazing purple")

# parmaters odering


def display_info(a, b, *args, instructor="Colt", **kwargs):
    # return [a, b, args, instructor, kwargs]
    print(type(args))


print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))

# a - 1
# b - 2
# args (3)
# instructor - "Colt"
# kwargs - {'last_name': "Steele", "job": "Instructor"}

[1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]

# unpacking tuples


def unpack(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)


nums = [1, 2, 3, 4, 5, 6,]  # to unpack this values
unpack(*nums)


# unpacking dictionary
def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "Colt", "second": "Rusty"}

# display_names(names)  # nope..
display_names(**names)  # yup!


def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)


data = dict(a=1, b=2, c=3, d=55, name="Tony")

add_and_multiply_numbers(**data)  # 7
add_and_multiply_numbers(**data, sam="green")  # 8
