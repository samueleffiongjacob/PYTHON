"""
    @iletrating or looping over dictionary

    method 1: .values collectors: this as to with values only
    method 2: .keys  collectors: this as to with key only
    method 3: .items collectors: this as to with key and values
    checking for key is dictionary
"""

# exampe method 1
name = {
    "NAME": "SAMUEL",
    "age": 32,
    "isMe": True}
print(name.values())

# let loop over it
for me in name.values():
    print(me)

# example method 2
db = {
    "class": "dictionary",
    "people": "order"
}
print(db.keys())

# let loop over it
for me in db.keys():
    print(me)

# example method 3
for v in name.items():
    print(v)

for q,w in db.items():
    print(q)
print(f"key is : {q} and value is {w}")

# checking for keys Dictionary 
gg = "class" in db
print(gg)

# checking for values Dictionary 
gg = "dictionary" in db.values()
print(gg)

# let loop over it 
mew = "dictionary" in db.values()
if mew:
    print(mew)
else:
    print("not true")