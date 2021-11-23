# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])   # "banana"

# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

thislist1 = ["apple", "banana", "cherry"]
print(thislist1[-1])  #cherry

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[2:5])   # ["cherry", "orange", "kiwi"]

# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[:4])   # ["apple", "banana", "cherry", "orange"]

#This example returns the items from "cherry" to the end:]
thislist5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist5[2:])  # ["cherry", "orange", "kiwi", "melon", "mango"]

# Range of Negative Indexes
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist6[-4:-1])   # ["orange", "kiwi", "melon"]

print("****************************************************************")

# Check if Item Exists
#  Check if "apple" is present in the list:
thislist7 = ["banana", "cherry"]
if "apple" in thislist7:
  print("Yes, 'apple' is in the fruits list")  # Yes, 'apple' is in the fruits list
else:
  print("No, apple is not present in the list")

print("****************************************************************")

# Change Item Value
thislist8 = ["apple", "banana", "cherry"]
thislist8[1] = "blackcurrant"
print(thislist8)  # ["apple", "blackcurrant", "cherry"]

# Change a Range of Item Values
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist9 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist9[1:3] = ["blackcurrant", "watermelon"]
print(thislist9)    # ["apple", "blackcurrant", "watermelon", "orange", "kiwi", "mango"]

# Change the second value by replacing it with two new values:
thislist11 = ["apple", "banana", "cherry"]
thislist11[1:2] = ["blackcurrant", "watermelon"]
print(thislist11)   # ["apple", "blackcurrant", "watermelon", "cherry"]

# Change the second and third value by replacing it with one value:
thislist12 = ["apple", "banana", "cherry"]
thislist12[1:3] = ["watermelon"]
print(thislist12)  # ["apple", "watermelon"]

# Insert Items
thislist13 = ["apple", "banana", "cherry"]
thislist13.insert(2, "watermelon")
print(thislist13)   # ["apple", "banana", "watermelon","cherry"]

# Append Items
# To add an item to the end of the list, use the append() method:
thislist14 = ["apple", "banana", "cherry"]
thislist14.append("orange")
print(thislist14)   # ["apple", "banana", "cherry", "orange" ]

#Extend List
# To append elements from another list to the current list, use the extend() method.
thislist16 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist16.extend(tropical)
print(thislist16)    # ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]

thislist17= ["apple", "banana", "cherry"]
thistuple1 = ("kiwi", "orange")
thislist.extend(thistuple1)
print(thislist17)

# Remove Specified Item
# The remove() method removes the specified item.
thislist18 = ["apple", "banana", "cherry"]
thislist18.remove("banana")
print(thislist18)  #  ["apple", "cherry"]

# Remove Specified Index
# The pop() method removes the specified index.
thislist19 = ["apple", "banana", "cherry"]
thislist19.pop(1)
print(thislist19)  # ["apple","cherry"]

# The del keyword also removes the specified index:
thislist21 = ["apple", "banana", "cherry"]
del thislist21[0]
print(thislist21) # [ "banana", "cherry"]

# Clear the List
thislist22 = ["apple", "banana", "cherry"]
thislist22.clear()
print(thislist22)  # []

# Loop Through a List  : Print all items in the list, one by one:
thislist23 = ["apple", "banana", "cherry"]
for x in thislist23:
  print(x)   # apple, banana, cherry : in one by one

print("********************* abadsfdsfs *******************************************")
# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.
thislist24 = ["apple", "banana", "cherry"]
for i in range(len(thislist24)):
  print(thislist24[i])

print("********************* abadsfdsfs *******************************************")

# Using a While Loop : Print all items, using a while loop to go through all the index numbers
list1 = ["apple", "banana", "cherry"]
i = 0
while i < len(list1):
  print(list1[i])
  i = i + 1   # # apple, banana, cherry : in one by one

print("****************************************************************************")
# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]     # **************************
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)    # ["apple", "banana", "mango"]

print("****************************************************************************")

fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits if x != "apple"]

print(newlist1)   # ["banana", "cherry", "kiwi", "mango"]

print("****************************************************************************")

# Expression: Set the values in the new list to upper case:
fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
#fruits3 = ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
newlist2 = [x.upper() for x in fruits2]
print(newlist2)  # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

print("****************************************************************************")

# Set all values in the new list to 'hello':
fruits7 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist4 = ['hello' for x in fruits7]
print(newlist4)    # ['hello', 'hello', 'hello', 'hello', 'hello']

print("****************************************************************************")

# Return "orange" instead of "banana":
fruits8 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist8 = [x if x != "banana" else "orange" for x in fruits8]
print(newlist8)   # ['apple', 'orange', 'cherry', 'kiwi', 'mango']

print("****************************************************************************")

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# Sort ascending
list21 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list21.sort()
print(list21)  # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

print("****************************************************************************")

# Sort Descending
list22 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list22.sort(reverse = True)
print(list22)  # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

print("****************************************************************************")
def myfunc(n):
  return abs(n - 50)
list23 = [100, 50, 65, 82, 23]
list23.sort(key = myfunc)
print(list23)    # [50, 65, 23, 82, 100]

print("****************************************************************************")

list24= ["z", "y", "x", "n", "m", "q", "p", "t", "v"]
list24.sort()
print(list24)

print("****************************************************************************")
# Case Insensitive Sort :
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
list25 = ["banana", "Orange", "Kiwi", "cherry"]
list25.sort()
print(list25)  #['Kiwi', 'Orange', 'banana', 'cherry']


print("****************************************************************************")
#Perform a case-insensitive sort of the list:
list26 = ["banana", "Orange", "Kiwi", "cherry"]
list26.sort(key = str.lower)
print(list26)   # ['banana', 'cherry', 'Kiwi', 'Orange']

print("****************************************************************************")
# Reverse Order
list27 = ["banana", "Orange", "Kiwi", "cherry"]
list27.reverse()
print(list27) # ['cherry', 'Kiwi', 'Orange', 'banana']

print("****************************************************************************")
# Copy a List
list27 = ["apple", "banana", "cherry"]
mylist1 = list27.copy()
print(mylist1)  # ['apple', 'banana', 'cherry']

print("****************************************************************************")
# Make a copy of a list with the list() method:
list28 = ["apple", "banana", "cherry"]
mylist2 = list(list28)
print(mylist2)  # ["apple", "banana", "cherry"]

print("****************************************************************************")
# Join Two Lists
list31 = ["a", "b", "c"]
list32 = [1, 2, 3]

list33 = list31 + list32
print(list33)    # ['a', 'b', 'c', 1, 2, 3]

# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3, 4, 5]
for x in list2:
  list1.append(x)
print(list1)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # ['a', 'b', 'c', 1, 2, 3]

#



























