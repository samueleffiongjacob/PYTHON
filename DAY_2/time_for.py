"""
    @looping theough times using for loop and range

    what is range : number of ocurrance in the function
"""

times = input("HOW MANY TIMES DID L ASK U TO CLEAN THE ROOM : \n")
times = int(times)

# just printing without count in front end
for time in range(times):
    print("CLEAN THE ROOM")

# just printing with counting in front end
for time in range(times):
    print(f"{time} CLEAN THE ROOM")

# just printing with counting in front end and remove 0
for time in range(times):
    print(f"{time + 1}: CLEAN THE ROOM")
