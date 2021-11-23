
# While Loops:
# Python has two primitive loop commands:
# 1. while loops
# 2. for loops

# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1  # 1, 2, 3, 4, 5  # Note: remember to increment i, or else the loop will continue forever.


print("************************************")
# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
i1 = 1
while i1 < 6:
  print(i1)
  if i1 == 3:
    break
  i1 = i1 + 1

print("************************************")
# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
i2 = 0
while i2 < 6:
  i2 = i2+ 1
  if i2 == 3:
    continue
  print(i2)   # 1, 2, 4, 5, 6

print("************************************")

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
i3 = 1
while i3 < 6:
  print(i3)
  i3 = i3 + 1
else:
  print("i is no longer less than 6") # 1, 2, 3, 4, 5, i is no longer less than 6


