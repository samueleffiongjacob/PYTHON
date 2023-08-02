"""
    @ SYNTAX below
    {__:__for__in__}

    iterate over keys by default
    to iterate over Keys and values using .items()

    @conditional logic i dictionary comprehension
"""

#  example 1
number = dict(first=1, second=2, third=3)
numbers = {"name": "samuel", "dick": "pussy", "enter": "me"}
# squred_numbers = {key:value **2 for key, value in number.items()}
squred_numbers = {key: value ** 2 for key, value in number.items()}

# chNGIN TO UPPER
upper = {k.upper(): v.upper() for k, v in numbers.items()}
upper1 = {k.upper(): v for k, v in number.items()}
print(f"this for upper and key upper : \n {upper} \n {upper1}")
# example 2
peras = {num: num**2 for num in [1, 2, 3, 4, 5]}

# example
str1 = 'ABC'
str2 = '123'
combo = {str1[i]: str2[i] for i in range(0, len(str1))}

print(
    f"this is first and second example: \n {squred_numbers} \n {peras}")
print(f'\n this is third example: {combo}')

# conditional
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 100]
number23 = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(f'this conditional for dictionary : \n {number23}')

# test out in range
rang = {num: ("even" if num % 2 == 0 else "odd") for num in range(1, 100)}
print(rang)

vluea = {(k.upper() if k is "str1" else k): v.upper() for k,v in numbers.items()}
print(vluea)