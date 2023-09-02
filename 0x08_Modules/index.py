from random import choice as pick, randint as r
from termcolor import colored  

print(pick(["apple", "banana", "cherry", "samuel"]))
print(r(1, 100))
text = colored("HI THERE!", color="magenta",
               on_color="on_cyan", attrs=["blink"])
print(text)
