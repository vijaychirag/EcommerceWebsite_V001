
# Accessing Items:
dict1 =	{"brand": "Ford","model": "Mustang","year": 1964}
print(dict1["model"])  # Mustang

# get() method:
dict2 =	{"brand": "Ford","model": "Mustang","year": 1964}
dict3 = dict2.get("year")
print(dict3)

# extract value from key()
dict4 =	{"brand": "Ford","model": "Mustang","year": 1964}
dict5 = dict4.keys()
print(dict5)   # dict_keys(['brand', 'model', 'year'])

# Get Values
dict6 =	{"brand": "Ford","model": "Mustang","year": 1964}
dict7 = dict6.values()
print(dict7)   # dict_values(['Ford', 'Mustang', 1964])

# Make a change in the original dictionary, and see that the values list gets updated as well:
dict8 =	{"brand": "Ford","model": "Mustang","year": 1964}
dict9 = dict8.values()
print(dict9)    # # dict_values(['Ford', 'Mustang', 1964])
dict8["year"] = 2020
print(dict8)   # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Get Items: The items() method will return each item in a dictionary, as tuples in a list.
dict11 = {"brand": "Ford","model": "Mustang","year": 1964}
dict12 = dict11.items()
print(dict12)  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])  list

# Check if Key Exists:
dict13 = {"brand": "Ford","model": "Mustang","year": 1964}
if "brand" in dict13:
    print("yes, brand key is present in dict13")

print("***************** Change Dictionary Items ************************")

dict14 = {"brand": "Ford","model": "Mustang","year": 1964}
dict14["brand"] = "TataMotors"
print(dict14)  # {'brand': 'TataMotors', 'model': 'Mustang', 'year': 1964}

# Update Dictionary;
dict15 = {"brand": "Ford","model": "Mustang","year": 1964}
dict15.update({"newcar": "Altroz"})
print(dict15)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}

print("***************** Remove Dictionary Items ************************")
# Remove Dictionary Items:
dict16 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}
dict16.pop("year")
print(dict16)  # {'brand': 'Ford', 'model': 'Mustang', 'newcar': 'Altroz'}

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
dict17 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}
dict17.popitem()
print(dict17)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# he del keyword removes the item with the specified key name:
dict18 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}
del dict18["model"]
print(dict18) # {'brand': 'Ford', 'year': 1964, 'newcar': 'Altroz'}

# The del keyword can also delete the dictionary completely:
dict19 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}
del dict19
#print(dict19)   # #this will cause an error because "thisdict" no longer exists.


# The clear() method empties the dictionary:
dict20 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}
dict20.clear()
print(dict20)

print("***************** Loop Through a Dictionary ************************")
dict21 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}
for x in dict21:
    print(x)  # it returns only key names

# You can also use the values() method to return values of a dictionary:
dict22 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}
for x in dict22.values():
    print(dict22)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}

dict23 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}
for x in dict23.keys():
    print(dict23)

dict24 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}
for x, y in dict24.items():
    print(x, y)

print("***************** Copy a Dictionary ************************")
# Make a copy of a dictionary with the copy() method:
dict24 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}
dict25 = dict24.copy()
print(dict25)   # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'newcar': 'Altroz'}

print("***************** Nested Dictionaries ************************")
myfamily = {"child1" : {"name" : "Emil","year" : 2004},"child2" : {"name" : "Tobias","year" : 2007},"child3" : {"name" : "Linus","year" : 2011}}

print(myfamily)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily2)












