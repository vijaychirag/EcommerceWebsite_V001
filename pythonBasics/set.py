# set: It is unordered, unindexed, immutable and does not allows duplicates:
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

set1 = {"unordered", "unindexed", "immutable or Unchangeable", "does not allow duplicates" , "unordered"}
print(set1)

# Get the Length of a Set
set22 = {"unordered", "unindexed", "immutable or Unchangeable", "does not allow duplicates" , "unordered"}
print(len(set22)) # 4, because it will not duplicate values in set

print(" *************************************** ")
set11 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(type(set11))  # <class 'set'>
print(set2)  # {1, 3, 5, 7, 9}
print(set3)  # {False, True}

print(" *************************************** ")
set4 = {"abc", 34, True, 40, "male"}
print(set4)

# Access Items : Loop through the set, and print the values:
set5 = {"apple", "banana", "cherry"}
for x in set5:
  print(x)

set6 = {"apple", "banana", "cherry"}
print("banana" in set6)   # True

print(" **************** add() *********************** ")
# Add Items

set7 = {"apple", "banana", "cherry"}
set7.add("mango and cherry")
print(set7)  # {'apple', 'cherry', 'mango and cherry', 'banana'}

# To add items from another set into the current set, use the update() method.


set8 = {"apple", "banana", "cherry"}
set9 = {'physics', 'chemistry', 1997, 2000}
set8.update(set9)
print(set8)  # {2000, 'banana', 'physics', 'cherry', 'apple', 1997, 'chemistry'}
print(set9)  # {2000, 'physics', 1997, 'chemistry'}


# To remove an item in a set, use the remove(), or the discard() method
# Note: If the item to remove does not exist, discard() will NOT raise an error.
set11 = {"apple", "banana", "cherry"}
set11.remove("banana")
print(set11)       # { "apple", "banana" }

set12 = {"apple", "banana", "cherry"}
set12.discard("banana")
print(set12)    # {'apple', 'cherry'}

# The return value of the pop() method is the removed item.
# Remember that sets are unordered, so you will not know what item that gets removed.
set13 = {"apple", "banana", "cherry"}
print(set13.pop())
print(set13)

set14 = {"apple", "banana", "cherry"}
x = set14.pop()
print(x) #removed item
print(set14) #the set after removal

# clear()
set15 = {"apple", "banana", "cherry"}
set15.clear()
print(set15)   # set()

#   Loop Items:
set16 = {'physics', 'chemistry', 1997, 2000}
for x in set16:
  print(x)

# Join Two Sets:
# The union() method returns a new set with all items from both sets:
set17 = {'physics', 'chemistry', 1997, 2000, "maths"}
set18 = {"apple", "banana","maths", "cherry"}
set19 = set17.union(set18)
print(set19)

# The update() method inserts the items in set2 into set1:
set21 = {'physics', 'chemistry', 1997, 2000, "maths"}
set22 = {"apple", "banana","maths", "cherry"}
set21.update(set22)
print(set21)  # {'maths', 'cherry', 1997, 2000, 'apple', 'physics', 'chemistry', 'banana'}
print(set22)  # {'cherry', 'apple', 'banana', 'maths'}


print("************ intersection, intersection_updates,symmetric_diff_updates **********************************")
# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)     #  { 'apple'}


# The intersection() method will return a new set, that only contains the items that are present in both sets.
x1 = {"apple", "banana", "cherry", "clustered apple", "pinaple"}
y1 = {"google", "microsoft", "apple", "clustered apple"}
z1 = x1.intersection(y1)
print(z1)                # {'apple', 'clustered apple'}

# Keep All, But NOT the Duplicates:
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}
x2.symmetric_difference_update(y2)
print(x2)       # {'cherry', 'banana', 'google', 'microsoft'}


# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x3 = {"apple", "banana", "cherry"}
y3 = {"google", "microsoft", "apple"}
z3 = x3.symmetric_difference(y3)
print(z3)        # {'google', 'microsoft', 'banana', 'cherry'}















