"""
    @List Methods Index, Count, Sort, Reverse, and Join

    @INDEX : it is use in finding a paticular position
    return the index of the specified item in the list
"""

SMA = ["FREDA", "DANIEL", "QUERY"]
sma = SMA.index("QUERY")
print(sma)

# specifing start and finish point
DANIEL = [1, 2, 3, 4, 5, 6, 5]
dan = DANIEL.index(5, 1)  # start counting from 1
print(dan)

SAMUEL = [1, 2, 3, 4, 5, 6, 5]
sam = SAMUEL.index(3, 2)  # start counting from 2
print(sam)

Aqw = [1, 2, 3, 4, 5, 6, 5]
awq = Aqw.index(5, 3, 6)  # start counting from 2 to 6
print(awq)

"""
    @count
    it accept a single input and give the output on how many times the
      varaible occurs
    it returns the number of times x appears in the list
"""
bda = [1, 2, 3, 4, 5, 6, 5, "FREDA", "DANIEL", "QUERY"]
bd = bda.count(5)  # Returns how many times 5 occures
bd1 = bda.count("QUERY")
print(bd, bd1)

"""
    @reverse
    it would reverse the other of they list
    reverse the other of the list
"""
sen = [1, 2, 3, 4, 5, 6, 5, "FREDA", "DANIEL", "QUERY"]
sen.reverse()  # reverse the other of the list
print(sen)  # not variable can't be reassign


""""
    @sort
    it sort things in accending oder
    sort the items of the (in-place)
"""

ge = [10, 2, 5, 4, 9, 3, 1, 6, 8, 7]
ge.sort()  # it sort things orderly or acending order and be reassign
print(ge)

ge1 = ["w", "r", 'y', 'q', 't', 'u', 'i', 'o', 'z', 'x', 'c', 'v',
       'b', 'n', 'm', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', "a"]
ge1.sort()  # it sort things orderly or acending order and be reassign
print(ge1)

"""
    @join : it use to join strings together
    technically a STRING Method that takes an iterable argument
    concatenates (combine) a copy of the base string between
        each item of the iterable
    returns a new string
    can be use to make sentences out of a list of words by
        joining on a space, for instance
"""

words = ['coding ', 'Is', 'Fun!']
hee = ' '.join(words)  # joins what ever u specified
print(hee)

names = ['Mr', 'Steal']
hee1 = '.'.join(names)  # joins what ever u specified
print(hee1)
