"""
    @pop : taking a single argument corresponding to key
            and removes that Key-value pair from the
            dictionary.Returns the value corresponding
            to the Key that was removed
    @popitems : removes a random Key in a dictionary
    @Update: Update Keys and values in a dictionary with
             another set of key value pair
"""

# example pop
d = dict(a=45, b=56, c=34)
# a = d.pop()  # TypeError: pop expected at least 1 arguments,got 0
b = d.pop('a')  # 45
print(d)
# e= d.pop('e' )  # KeyError

# example for pop Item
mys = dict(a=45, b=56, c=34)
ds = mys.popitem()  # c('d', 4)
# TypeError: pop expected at least 1 arguments,(1 given)
# da = mys.popitem('a')

# example update
p = dict(f=45, k=56, c=34)
second = {}

second.update(p)
print(p)
perosn = {}
perosn.update(p)
# overiding existing a
perosn['a'] = 'AMAZING'
perosn.update(p)
print(perosn)
