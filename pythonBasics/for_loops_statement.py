# For Loops:
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String:
for x in "banana":
  print(x)

print("*************break statement ***************************")
# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
fruits1 = ["apple", "banana", "cherry"]
for x in fruits1:
  print(x)
  if x == "banana":
    break              # apple  , banana

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits2 = ["apple", "banana", "cherry"]
for x in fruits2:
  if x == "banana":
    break
  print(x)         # apple

print("************* continue statement ***************************")
# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits3 = ["apple", "banana", "cherry"]
for x in fruits3:
  if x == "banana":
    continue
  print(x)    # apple   cherry

print("************* range() Function ***************************")
# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.

for x in range(6):
  print(x)   # 0, 1, 2, 3, 4, 5

# Using the start parameter:
for x in range(2, 6):
    print(x)  # 2, 3, 4, 5

# The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

for x in range(2, 30, 3):
  print(x) # 2, 5, 8, 11, 14, 17, 20, 23, 26, 29

print("************* range() Function ***************************")
# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
  print(x)
else:
  print("Finally finished!") # 0, 1, 2, 3, 4, 5 Finally finished!


# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")   # 0 1 2

print("************* Nested Loops ***************************")
# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)   # red apple, red banana, red cherry, big apple, big banana, big cherry, tasty apple, tasty banana, tasty cherry.

print("************* pass Statement ***************************")
# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.







