# RegEx(Regular expression) It is a sequence of character that forms a search pattern.

'''RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	 :Returns a list containing all matches
search	 :Returns a Match object if there is a match anywhere in the string
split	 :Returns a list where the string has been split at each match
sub	     :   Replaces one or many matches with a string'''

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")   # YES! We have a match!

print("****************************************")

#Find all lower case characters alphabetically between "a" and "m":
txt1 = "The rain in Spain"
x1 = re.findall("[a-m]", txt1)
print(x1)  # ['h', 'e', 'a', 'i', 'i', 'a', 'i']

print("****************************************")

#Find all digit characters:
txt2 = "That will be 59 dollars"
x2 = re.findall("\d", txt2)
print(x2)  # ['5', '9']

print("****************************************")
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

txt3 = "hello planet"
x3 = re.findall("pl...t", txt3)
x31 = re.findall("he..o", txt3)
print(x3)   #['planet']
print(x31)   # ['hello']

print("****************************************")

#Check if the string starts with 'hello':
txt4 = "hello planet"

x4 = re.findall("^hello", txt4)  # Yes, the string starts with 'hello'
if x4:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

print("****************************************")

#Check if the string ends with 'planet':
txt5 = "hello planet"
x5 = re.findall("planet$", txt5)  # Yes, the string ends with 'planet'
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

print("****************************************")

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
txt6 = "hello planet"
x6 = re.findall("he.*o", txt6)
print(x6) # ['hello']

print("****************************************")

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
txt7 = "hello planet"
x7 = re.findall("he.+o", txt7)
print(x7)  # ['hello']

print("****************************************")

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
txt8 = "hello planet"
x8 = re.findall("he.?o", txt8)
print(x8)  # []
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o

print("****************************************")

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
txt9 = "hello planet"
x9 = re.findall("he.{2}o", txt9)
print(x9)  # ['hello']

print("****************************************")

# Special Sequences
#Check if the string starts with "The":
txt11 = "The rain in Spain"
x11 = re.findall("\AThe", txt11)
print(x11)
if x:
  print("Yes, there is a match!")
else:
  print("No match")  # ['The']
                     # Yes, there is a match!

print("****************************************")

#Check if the string contains any digits (numbers from 0-9):
txt12 = "The rain in Spain"
x12 = re.findall("\d", txt12)
print(x12)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")  # []
                     # No Match

print("****************************************")

#Return a match at every no-digit character:
txt13 = "The rain in Spain"
x13 = re.findall("\D", txt13)
print(x13)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")  #['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n']
                    # Yes, there is at least one match!

print("****************************************")

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
txt = "The rain in Spain"
x = re.findall("\w", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

print("****************************************")

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
txt14 = "Therain in Spain"
x14= re.findall("\W", txt14)
print(x14)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")   # [' ', ' ']
                      # Yes, there is at least one match!

