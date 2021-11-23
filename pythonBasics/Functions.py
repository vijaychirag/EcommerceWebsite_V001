# In python, function is a group of related statements, that performs specific tasks.
# Recursion: Python also accepts function recursion, which means a defined function can call itself.
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# In Python a function is defined using the def keyword:


#Function declaration: or creating function

def GreetMe(name):
    print("hello world " + name)

# passing parameters into the function:
def summation(a, b):
    print(a+b)

def sum(c,d):
    return c+d

# calling a function:
GreetMe("python")   # hello world python
summation(3, 5)    # 8
print(sum(4, 8))  # 12

print("***************************************************************")
# Creating a Function:
def my_function():
  print("Hello from a function")

# Calling a Function:
def my_function1():
  print("Hello from a function")

my_function1()  # Hello from a function

print("********************* Arguments ******************************************")
# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.

def my_function2(fname):
  print(fname + " References")

my_function2("Emil")   # Emil References
my_function2("Tobias")  # Tobias References
my_function2("Linus")  # Linus References

print("********************* Parameters or Arguments? ******************************************")
# Parameters or Arguments?
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def my_function3(fname, lname):
  print(fname + " " + lname)
my_function3("Emil", "Refsnes")  # Emil Refsnes

print("********************* Arbitrary Arguments, *args ******************************************")
# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name:
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function4(*kids):  # parameters
  print("The youngest child is " + kids[2])

# below are the arguments
my_function4("Emil", "Tobias", "Linus")  # The youngest child is Linus

print("********************* Keyword Arguments: ******************************************")
# Keyword Arguments:

def my_function5(child3, child2, child1):
  print("The youngest child is " + child3)

my_function5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")  # The youngest child is Linus

print("*********************  Keyword Arguments, **kwargs ******************************************")
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function6(**kid):
  print("His last name is " + kid["lname"])

my_function6(fname = "Tobias", lname = "Refsnes")

print("*********************  Default Parameter Value ******************************************")
# Default Parameter Value
def my_function7(country = "Norway"):
  print("I am from " + country)

my_function7("Sweden")  # I am from Sweden
my_function7("India")  # I am from India
my_function7()   # I am from Norway
my_function7("Brazil")  # I am from Brazil

print("*********************  Passing a List as an Argument ******************************************")
# Passing a List as an Argument
def my_function8(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function8(fruits)

print("*********************  Return Values ******************************************")
# Return Values
def my_function9(x):
  return 5 * x

print(my_function9(3))  # 15
print(my_function9(5))  # 25
print(my_function9(9))  # 45

print("*********************  Recursion ******************************************")
# Recursion: which means a defined function can call itself.
# Recursion is a mathematical and programming concept. It means that a function calls itself.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)







