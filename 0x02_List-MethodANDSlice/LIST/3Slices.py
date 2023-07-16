"""
    @Slicing starting
    it as to do with making a new list from the old one
    e.g: my_list[start: end : step]
"""

# FIRST PARAMATER: IT MUST INCLUDE COLUMN :
My_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
me = My_list[1:]  # start slicing from 1
me1 = My_list[9:]  # start slicing from 3
me2 = My_list[20:]  # start slicing from 20

# SLICING WITH NEGATIVE NUMBERS
# nagative takes the reverse order of counting from the end or countin backwars
me3 = My_list[-3:]

# nagative takes the reverse order of counting from the end
me4 = My_list[-10:]
m5 = My_list == me  # checking to see if the slicing refrences a list
m6 = My_list is me  # TESTING MEMORY ALLOCATION

print(me, me1, me2, me3, me4, m5, m6)

"""
    @end Slicing
"""
# we end by adding columb to the end
me7 = My_list[:-10]
me8 = My_list[:10]
print(me7, me8)

"""
    @steps in slicing
    in python is basically the number to count at a time
    same as step with range!
    for example:  STEP OF 2 count every other number(1,2,4)
"""
mee = My_list[1::2]  # no midlle means there is no end just steps
mee1 = My_list[::2]  # no midlle means there is no end just steps
mee2 = My_list[1::-1]  # negative other or reverse
mee3 = My_list[:1:-1]  # negative other or reverse
mee4 = My_list[2::-1]  # negative other or reverse
print(mee, mee1, mee2, mee3, mee4)


"""
    @string slicing
"""

string = "this is fun!"
mee5 = string[::-1]

# Modifying portions of lists
My_list[1:3] = ['a', 'b', 'c']
print(mee5, My_list)
