# A regular named function
def square(num): return num * num


# An equivalent lambda, saved to a variable
def square2(num): return num * num


# Another lambda
def add(a, b): return a + b


# Executing the lambdas
print(square2(7))
print(add(3, 10))

# Notice that the square function has a name, but the two lambdas do not
print(square.__name__)
print(square2.__name__)
print(add.__name__)


# example 2 on lambda 
import tkinter as tk
root = tk.tk() # creaating environment for running
frame = tk.Frame(root) # creating frame
frame.pack() ## creating a block for the design

# Don't need this function if we use a lambda 
# def say_hi():
#     print("HELLO!")

button = tk.Button(frame, text= "CLICK ME", fg="green", command= lambda : print("SAMUEL IS GOOD "))
button.pack(side=tk.RIGHT)
root.mainloop()