# Tuple: Tuple is sequence type data type and it is a collection of objects,
# which is ordered, immutable, it allows duplicates.

# Accessing Values in Tuples:
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print (tup1[0])   # physics
print (tup2[1:5])   # (2, 3, 4, 5)


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# Updating Tuples
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
#tup1[0] = 100
#print(tup1)

# So let's create a new tuple as follows
# concatination:
tup3 = tup1 + tup2
print (tup3)           # (12, 34.56, 'abc', 'xyz')

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# Delete Tuple Elements

tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
print ("After deleting tup : ")
#print(tup)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# Python Expression
# Indexing, Slicing, and Matrixes:
L = ('spam', 'Spam', 'SPAM!')
print(L[2])  # 'SPAM!'
print(L[-2])  # 'Spam'
print(L[1:])   # ('Spam', 'SPAM!')   # it returns list

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
tuple1 = ("apple", "banana", "cherry")
print(type(tuple1))  # <class 'tuple'>

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
tuple2 = tuple(("apple", "banana", "cherry"))
print(tuple2)   # ("apple", "banana", "cherry")

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# Access Tuple Items
tup11 = ("apple", "banana", "cherry")
print(tup11[1])  # banana

# Negative Indexing : Print the last item of the tuple:
tup4 = ("apple", "banana", "cherry")
print(tup4[-3]) # apple

# Range of Indexes: Return the third, fourth, and fifth item:
tup5= ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tup5[2:5]) # ('cherry', 'orange', 'kiwi')

# This example returns the items from the beginning to, but NOT included, "kiwi":
tup6 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tup6[:4])  # ("apple", "banana", "cherry", "orange")

# This example returns the items from "cherry" and to the end:
tup7 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tup7[2:])  # ("cherry", "orange", "kiwi", "melon", "mango")

# Range of Negative Indexes
tup8 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tup8[-4:-1])   # ("orange", "kiwi", "melon")

# Check if "apple" is present in the tuple:
tup9 = ("apple", "banana", "cherry")
if "apple" in tup9:
  print("Yes, 'apple' is in the fruits tuple")
else:
    print("no, apple is not in the fruits")    # "Yes, 'apple' is in the fruits tuple"

print("^^^^^Update Tuples starts^^^^^^^^^^")
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)   # ('apple', 'kiwi', 'cherry')

# Convert into a list
tup11 = ("apple", "banana", "cherry")
y = list(tup11)
y.append("orange")
tup11 = tuple(y)
print(tup11)   # ('apple', 'banana', 'cherry', 'orange')

# 2. Add tuple to a tuple
tup12 = ("apple", "banana", "cherry")
y = ("orange",)
tup12 += y     # tup12 = tup12 + y
#tup13= tup12 + y
print(tup12)

# Note: You cannot remove items in a tuple.
tup14 = ("Everything", "possible", "Unless")
var1 = list(tup14)
var1.remove("possible")
tup14 = tuple(var1)
print(tup14)

# The del keyword can delete the tuple completely:
tup15 = ("Everything", "ispossible", "Unless")
del tup15
#print(tup15)

print("%%%%%%%%%%%%%%%%%%%% packing starts %%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# packing a Tuple
tup16 = ("oosaka", "fugimountain", "tokyo")
print(tup16)

# Unpacking a Tuple
cricket = ("RahulDravid", "Virat", "k.Williamson")
GentleMan, AggressiveCricketer, BestCaptain = cricket
print(GentleMan)        # RahulDravid
print(AggressiveCricketer)  #Virat
print(BestCaptain)   # k.Williamson

print("*************very imp concept unpacking in tuple *****************")
# The number of variables must match the number of values in the tuple, if not,
# you must use an asterisk to collect the remaining values as a list.

cricketers = ("RahulDravid", "Virat", "Dhoni", "k.Williamson", "Ganguly")
GentleMan, *AggressiveCricketer, BestCaptain = cricketers
print(GentleMan)        # RahulDravid
print(AggressiveCricketer)  #Virat
print(BestCaptain)     # ['Dhoni', 'k.Williamson', 'Ganguly']

# Add a list of values the "Gentlemen" variable:
cricketers1 = ("RahulDravid", "Virat", "Dhoni", "k.Williamson", "Ganguly")
*GentleMan, AggressiveCricketer, BestCaptain = cricketers1
print(GentleMan)        # ['RahulDravid', 'Virat', 'Dhoni']
print(AggressiveCricketer)  # k.Williamson
print(BestCaptain)     # Ganguly

print("*************loop through the index numbers *****************")
# Loop Through the Index Numbers : Use the range() and len() functions to create a suitable iterable.
cricketers2 = ("RahulDravid", "Virat", "Dhoni", "k.Williamson", "Ganguly")
for i in range(len(cricketers2)):
    print(cricketers2[i])

cricket3 = ("RahulDravid", "Virat", "Dhoni", "k.Williamson", "Ganguly")
for x in cricket3:
    print(x)

# Using a While Loop:
# Use the len() function to determine the length of the tuple, then start at 0 and
# loop your way through the tuple items by refering to their indexes.
# note: Remember to increase the index by 1 after each iteration. ##################

technologies = ( "machinlearning", "AitrificialIntelligency", "Datascienc" )
k = 0
while k < len(technologies):
    print(technologies[k])
    k = k + 1

print("*************Join Two Tuples *****************")
# Join Two Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3, 9.5)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
frameworks = ("pytest", "unittest", "robot")
print(frameworks*2)   # ('pytest', 'unittest', 'robot', 'pytest', 'unittest', 'robot')
# newfra = (frameworks*2)











