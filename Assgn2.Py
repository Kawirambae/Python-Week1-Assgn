# Code Challenge:
# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
# Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
# Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
# Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
# 1.
# my_list = input("Please input a list of integers")
# my_list = list(map(int,my_list.split()))
# Result = sum(my_list)
# print(Result)
# 2. 
# #my_tuple = ("Gone with the wind", "A court of thorns and Roses", "In the name of the wind", "Siddharta", "Conversations with God")
# # for item in my_tuple:
# #  print(item)
#  3.
# person = {}
# person["name"] = input("please enter your name:")
# person["age"] = int(input("please enter your age:"))
# person["marital status"] = input("please enter your marital status:")
# person["vote"] = input("please enter your slogan vote:")
# print("\n User Information:")
# print(person)

# 5.
# my_hobbies = ["reading", "swimming", "travelling"]
# odd = [word for word in my_hobbies if len(word) % 2 != 0]
# print(odd)

# Assignment:
# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.

1. 
# my_list = []
# my_list.append([50,60,70])
# print(my_list)
# my_list[0].insert(1,15)
# print(my_list)
# my_list.extend((50,60,70))
# print(my_list)
# last_number = my_list.pop()
# print(my_list)
# my_list.sort()
# print(my_list)
my_list = []
my_list.extend([50, 15, 60, 70])  
print(my_list)

my_list.extend([50, 60, 70]) 
print(my_list)

my_list.pop()  
print(my_list)

my_list.sort()  
print(my_list)
if 30 in my_list:
    index_30 = my_list.index(30)
    print("Index of 30:", index_30)
else:
    print("Value 30 not found in my_list")