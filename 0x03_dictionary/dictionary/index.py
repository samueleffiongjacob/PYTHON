"""
    @dictionary as to do with key value pair
        it stores data in key value pair

    @Accessing dictionary through it key value pair
"""

# fist way to define a dictionary
name = {
    "NAME": "SAMUEL",
    "age": 32,
    "isMe": True}
print(f"starting out dictionary: \n {name}")

db = {
    "class": "dictionary",
    "people": "order"
}
print(db)

# second way to enter a dictionary:
value = dict(names="effiong", age="values")
# not recommended
print(value)

# key value pair useing list
me = name["NAME"]
print(me)
