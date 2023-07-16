"""
    @ METHOD
    @List Methods Append, Insert, and Extend
    appending data to and exiting list
    inserting data to and exiting list
    Extend data to and exiting
"""

# append and one item to the list
SMA = ["FREDA", "DANIEL", "QUERY"]
SMA.append(1)
print(SMA)

# extend and mutiple item to the list
sma = ["sam", "ewa"]
sma.extend(["samuel", "asdas", "qwerty", 1, 2, 3, 4, 5,])
print(sma)

# insert an item in a position of the list
dsa = ["WEA", "WER", "EREW", "QWERRE"]
dsa.insert(1, "WEA")
print(dsa)

# insert an item in a position of the list
dsa1 = [1, 2, 3, 4, 5, 6]
dsa1.insert(4, "WEA")
print(dsa1)
