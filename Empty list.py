# Create an empty list
my_list = []
# Append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# Insert the value 15 at the second position
my_list.insert(1,15)
# Extend my_list with another list
my_list.extend([50,60,70])
# Remove the last element from my_list
my_list.pop()
# Sort my_list in ascending order
my_list.sort()
# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
# Print the final list and the index of 30
print("Final List:", my_list)
print("Index of 30:", index_of_30)