"' A COnverter program works well'"

print("How many kilometer did you run today ?")  # Asking a qustion
kms = input()  # collecting user input
mile = float(kms)/1.60934  # operation to coverte into miles
mile = round(mile, 2)  # round up miles to 2 decimal place

print(f"Your  {kms} kilometers ride was {mile} mi\n")  # final out
