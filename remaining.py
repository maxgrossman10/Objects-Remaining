# %%
print("How many objects do you want from the set?")
objects = input()
objects = int(objects)
print("How many objects are in the set?")
set = input()
set = int(set)
number = set - objects
number = int(number)
print(f"The number of objects still remaining in the set is {number}!!")

# If this code is run without lines 4, 7, and 9, an error occurs claiming that it cannot perform mathmatical operations
# with strings. The issue was resolved by mandating that number, objects, and set all be integers. 