# starting out tuple
sam = ('a', 'b', 'c', "d")
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
cat = {"name": "biscuit", "age": 0.5, "favorite_toy": "my chapstick"}
bf = cat.items()
print(bf)

months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

# using for loops
for month in months:
    print(month)

# using while
i = len(months) - 1
while i >= 0:
    print(f" \n {months[-i]}")
    i -= 1

# nested tuples


nums = (1, 2, 3, (4, 5), 6, 7)
print(nums[3])  # (4,5)

# get 5 from  index3
print(nums[3][1])  # 5

# we use slices
print(nums[0:])  # (1,2,3,(4,5),6,7)

print(nums[0:4])  # (1,2,3,(4,5))

print(nums[0:4:2])  # (1,3)
