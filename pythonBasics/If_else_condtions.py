# Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.
# An "if statement" is written by using the if keyword.

a = 33
b = 200
if b > a:
  print("b is greater than a")

# Elif
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a1 = 33
b1 = 33
if b1 > a1:
  print("b1 is greater than a1")
elif a1 == b1:
  print("a1 and b1 are equal")  # "a1 and b1 are equal")

# Else
# The else keyword catches anything which isn't caught by the preceding conditions.
a2 = 200
b2 = 33
if b2 > a2:
  print("b2 is greater than a2")
elif a2 == b2:
  print("a2 and b2 are equal")
else:
  print("a2 is greater than b2")   # a2 is greater than b2

# Short Hand If
a3 = 200
b3 = 33
if a3 > b3: print("a3 is greater than b3")


# Short Hand If ... Else
a4 = 2
b4 = 330

print("A") if a4 > b4 else print("B")

# The and keyword is a logical operator, and is used to combine conditional statements:
a5 = 200
b5 = 33
c5 = 500
if a5 > b5 and c5 < a5:
  print("Both conditions are True")
else:
    print("b5 is lesser than a5 and c5")  # b5 is lesser than a5 and c5

# The or keyword is a logical operator, and is used to combine conditional statements:
a6 = 200
b6 = 33
c6 = 500
if a6 > b6 or a6 > c6:
  print("At least one of the conditions is True")

# Nested If
# You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")  # Above ten,  and also above 20!

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
a7 = 33
b7 = 200
if b7 > a7:
  pass


