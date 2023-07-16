"""
    @2List Comprehension With Conditional Logic
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [evens for evens in nums if evens % 2 == 0]
odd = [odds for odds in nums if odds % 2 != 0]
# 1/2 conditional
else1 = [num * 2 if num % 2 == 0 else num/2 for num in nums]
print(
    f"this is for even : {even} \n This is for odds : {odd} \n finally this is for else {else1} \n ==========================================")

# for string
with_vowels = "This is so much fun!"
with_vowels1 = "".join(char for char in with_vowels if char not in "aeiou")
print(with_vowels1)
