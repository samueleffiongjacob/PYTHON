"""
    @11. Nested Lists
    the ability to nest a values into an exiting list
    we can call them multi dimensional
"""
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ACCESSING THE FIRST BRACKET
# the first 0 we accesing the first braket and second element 2
nested1 = nested[0][1]

# the second 0 we accesing the first braket and last
# element using negative index
nested2 = nested[1][-1]
print(nested1, nested2)


"""
    @nested loops
"""
# ==========================================================================
nested3 = [['a', 'b', 'c'], ['d', 'e', 'g'], ['H', 'J', 'I']]
for qq in nested3:
    for val in qq:
        print(f"{val}")

# NESTED LIST COMPREHENSION
[[print(val) for val in P] for P in nested3]
# =====================================================================================

room = [[num for num in range(1, 4)] for val in range(1, 4)]

room1 = [["X" if num % 2 != 0 else "O" for num in range(
    1, 4)] for val in range(1, 4)]
print(room1, room)
