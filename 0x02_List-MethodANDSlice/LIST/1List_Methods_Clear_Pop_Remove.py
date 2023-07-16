"""
    @ List Methods Clear, Pop, and Remove,
"""

"""
    @clear
    remove all items from the list
"""

Name_lists = ["SAM", "LINDA", "jerry", "moses", "favour"]
Name_lists.clear()
print(Name_lists)


"""
 @pop method
 REmove the item at the given position in the list, and return it.
 if no index is specifield, removes and returns last items in the list

"""

Name_list = ["SAM", "LINDA", "jerry", "moses", "favour"]
Name_list.pop()  # it removes "favour"
print(Name_list)

Name_lists1 = ["SAM", "LINDA", "jerry", "moses", "favour"]
Name_lists1.pop(1)  # it would remove "linda"
print(Name_lists1)


"""
    @pop
    capturing removed pop
"""
Name_lists2 = ["SAM", "LINDA", "jerry", "moses", "favour"]
capture = Name_lists2.pop(0)  # assign sothat it could be useeful
print(capture, Name_lists2)


"""
    @remove
    Remove the first item from the list whose value is x
    Throws a valueError if the item is not found.
    very useful if u want to revome something the list and u are not sure were it is
    note the remove function does not return the value remove
"""
first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove = first_list.remove(2)  # remove exact value
print(first_list, remove)


first_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
remove1 = first_list1.remove(10)
print(first_list1, remove1)


Name_lists00 = ["SAM", "LINDA", "jerry", "moses", "favour"]
remove2 = Name_lists00.remove("moses")
print(remove2, Name_lists00)
