"""
Demo-Conditionals (BANANA)
"""
banana=int(input("How many banana do you have?: "))
print("You have {} banana(s)".format(banana))
print("")

if banana in range(1,5):
    print("That's a small bunch of bananas.")
elif(banana > 4):
    print("Wow! What a bunch of bananas.")
elif(banana==0):
    print("No banana, no pishang.")
#Problem down below-30/1/2022
else:
    print("Your banana count is weird. Please enter right input.")
    