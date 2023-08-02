"""
    @Dictionary Methods Clear, Copy, Fromkeys, and Get
     Clear : it empty the keys and values in a dictionary
     Copy  : makes a copy of a dictionary
     fromKeys: creates Key-valeus pairs from comma separated values
     Get: retrives a key in an object and return None
          instead of a KeyError if the Key does not exit
"""
# varible daeclear
a = dict(a=1, b=2, c=3)

# Copy example
b = a.copy()

# clear example :
c = dict(a=1, b=2, c=3)
c.clear()
print(f"this the copy dictionary:\n {b} \n this the cleared :\n {c}")

# testing memory
clone = a == b
clone1 = a is b
print(f"{clone} \n {clone1}")

# fromKeys very useful in db
new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], '')
print(new_user)
new_user2 = {}.fromkeys(range(1, 10), "unknow")
print(new_user2)

# get
new_get = a.get("a")
print(new_get)
new_grt1 = a.get('no_key') # if key does not exits it gives us non
print(new_grt1)
