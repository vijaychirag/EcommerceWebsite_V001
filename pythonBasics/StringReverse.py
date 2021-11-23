# Accessing Values in Strings

var1 = 'Hello World!'
var2 = "Python Programming"

print("var1[0]: ", var1[0])           #  H
print("var2[1:5]: ", var2[1:5])       #  ytho

print("**************************************************************************************")

# Updating Strings
var1 = 'Hello World!'
print("Updated String :- ", var1[:6] + 'Python')    # Hello Python
print("Updated String :- ", var2[6: ] + ' interp')  # Python interp

print("**************************************************************************************")

# reverse the strings
txt = "Hello World"[::-1]
print(txt)

txt1 = "Hello python"[::-1]
print(txt1)

#  [] Slice - Gives the character from the given index
a = "vijayakumar"
print(a[3:]+ " " + a[0:3])  # ayakumar vij
print(a[::-1])   # ramukayajiv

# [ : ] Range Slice - Gives the characters from the given range
jay = "pytest unitest framework"
print(jay[3:9])    # est un

# Triple Quotes
#'''Python's triple quotes comes to the rescue by allowing strings to span
# multiple lines, including verbatim NEWLINEs, TABs, and any other special characters.'''
 #The syntax for triple quotes consists of three consecutive single or double quotes.

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)

print ('C:\\nowhere')


print("**************************************************************************************")
# Repetition - Creates new strings, concatenating multiple copies of the same string

var7 = "selenium testing"
#print(var7*2)
print(var7.format())
#print(var7)


print("**************************************************************************************")
list1 = [1, 2, 3, 4, 5, 6]
list1.reverse()

# split method: it splits strings into substrings and retursn list
a = "hello world"
print(a.split(","))  # ["hello", "world"]

studentNames = ["Hannah", "Imogen", "Lewis", "Peter"]
print(studentNames[1])

studentNames = ["Hannah", "Imogen", "Lewis", "Peter"]
print(studentNames[1:3])

studentNames = ["Hannah", "Imogen", "Lewis", "Peter"]
print(studentNames[::-1])

studentNames = ["Hannah", "Imogen", "Lewis", "Peter"]
studentNames.reverse()
print(studentNames)

print("**************************************************************************************")

# string methods
 # count(), find(), format(), index(), join(), replace(), split(), strip()

# Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()
print(x)

# Replace the character H with a J.
txt5 = "Hello World"
txt6 = txt5.replace("H", "J")
print(txt6)

#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt8 = "My name is John, and I am {}"
print(txt8.format(age))






