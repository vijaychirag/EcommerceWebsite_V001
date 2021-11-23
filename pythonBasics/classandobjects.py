# Create Object
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

# The __init__() Function: Constuctor
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
# Note: The self parameter is a reference to the current instance of the class,
#         and is used to access variables that belong to the class.
class Person:
  def __init__(self, name, age): # instance variable
    self.name = name
    self.age = age

# object creation for class
p1 = Person("John", 36)   # arguments

print(p1.name)  # John
print(p1.age)  # 36

print("************ constuctor *****************************")
# Object Methods:
class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc1(self):
    print("Hello my name is " + self.name)

p1 = Person1("John", 36)
p1.myfunc1()                   # Hello my name is John

class Person2:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc2(abc):
    print("Hello my name is " + abc.name)

p1 = Person2("John", 36)
p1.myfunc2()             # Hello my name is John

print("************ Modify Object Properties *****************************")
# Modify Object Properties
class Person4:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc4(self):
    print("Hello my name is " + self.name)

p1 = Person4("John", 36)
p1.age = 40
print(p1.age)  # 40

# Delete Object Properties:
class Person5:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc5(self):
    print("Hello my name is " + self.name)

p1 = Person5("John", 36)
del p1.age
#print(p1.age)
# Traceback (most recent call last): AttributeError:

print("************ The pass Statement *****************************")
# class definitions cannot be empty,put in the pass statement to avoid getting an error.
class Person:
  pass
