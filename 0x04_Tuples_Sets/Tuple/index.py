# starting out tuple 
sam = ('a','b','c',"d")
type = type(sam)
print(type)

# Tuples can be be used as key in dictionairies

locations = {
    (35.6895, 39.6917): "Tokoyo office",
    (40.7128, 74.0060): "New York office",
    (37.7749, 122.4194): "San Francisco Office"
}

log = locations[(40.7128, 74.0060)]
print(log)

# Some dictionary method like .items() return tuples
cat = {"name": "biscuit", "age":0.5, "favorite_toy":"my chapstick"}
bf = cat.items()
print(bf)

months = ('January', 'February', 'March','April', 'May', 'June', 'July','August', 'September','October','November', 'December')

# using for loops
for month in months:
    print(month)

# using while
i = len(months) - 1
while i >= 0:
    print(f" \n {months[-i]}")
    i -= 1