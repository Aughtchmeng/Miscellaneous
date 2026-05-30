# Please note future Hoang, that this is used as a reference.
#Not as an actual code to execute, even you could that would be messy.
# just copy and paste line(s) into a Python server or smth.

x = "My family takes a vacation to the beach every year now." # Examples: Lines 1 & 2 
y = "They always go to Galveston." 
h = "Hello my friends." #Saved for different line or new file on hoang100's computer.

print(x +  " "  + y) # string concatenation, and there are many ways to add strings!

print("Hello"); print("How are you?"); print("Bye bye!") # A way of writing seperated strings on a different line.

print(x, end="") # Another way of making the string end on a single line
print(y, end="")

print("Hello\nWorld") # One word is one line, another is on another line. Can you guess which?

#Backward slashes also can be used to include other symbols or words inside a string.

print("She said \"Hello\" to me") # She said "Hello" to me
print('It\'s a nice day') # It's a nice day
print("This is a backslash: \\") # This is a backslash: \

# Example:

txt = "We are the so-called \"Vikings\" from the north."  # <=== Example

# Escape Characters: 
print("Hello\rWorld") # Moves the cursor back to the start of the line: World

print("Hello\tWorld") # Adds a tab space between words: Hello    World

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) # HelloWorld!

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# "Hello" & 'Hello' are the same thing.

#Quotes in a string are perfectly okay, as long as they don't match the outer ones:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Usage of triple stringed quotes
#line 36 will be line 1 on the console, downwards is line 2, and so on...)

z = '''Lorem ipsum dolor sit amet,  
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(z)

s = "Hello, World!"
print(s[1]) #This will retrieve index 1 of the string, which is not the first letter. Instead, the first letter is index 0.

# Strings == Arrays

for x in "banana":
  print(x)
# For every letter in this string, each line from top to bottom will be in the string's written order from left to right.

# Built in len() function: returns how many letters in a string. But not only for strings..?

a = "Hello, World!"
print(len(a))


# Conditionals: I must adhere to knowing the definitions and usages of sequences, events, conditionals, and loops before proceeding.

txt5 = "The best things in life are free!"
if "free" in txt5:
  print("Yes, 'free' is present.")

txt5 = "The best things in life are free!"
if "expensive" not in txt5:
  print("No, 'expensive' is NOT present.")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Sliced Strings

b = "Hello, World!"
print(b[2:5]) 
# Starts from a specific index and ends on another, in this case: llo
# It will start from the specified index, and end a index early before the last.

    
#Prints characters from position 0 to position 5.
b = "Hello, World!"
print(b[:5])


#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

#Diagram:

   #Character:  H  e  l  l  o  ,     W  o  r  l  d  !
   #Positive:   0  1  2  3  4  5  6   7  8  9  10 11 12
   #Negative:  -13-12-11-10 -9 -8 -7  -6 -5 -4  -3 -2 -1

b = "Hello, World!"
print(b[-5:-2])

#You can see that position starts from -5 and ends on -3; 'orl'

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Turns the entire string into uppercase.
b = "Hello, World!"
print(b.upper())

#Turns the entire string into lowercase.
b = "Hello, World!"
print(b.lower())

# Actual good use of strip() function
txt = ",,,,,rrttgg.....banana....rrr"

l= txt.strip(",.grt")

print(l)

#Replace()

a = "Hello, World!"
print(a.replace("H", "J"))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# F-Strings are usedto combine variables with strings
age = 36
txt2  = f"My name is John, I am {age}"
print(txt2)

# Display price with 2 decimals '.00'
price = 59
txt1 = f"The price is {price:.2f} dollars"
print(txt1)

# You could also perform basic arithmetic in that square brackets.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Miscallaneous String Functions:

# Capitalize() - The first character is converted to upper case, and the rest are converted to lower case:
txt = "python is FUN!"

x = txt.capitalize()

print (x)

# Casefold() - Make the string lower case:
tt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

# Center() - The center() method will center align the string, using a specified character (space is default) as the fill character.
# string.center(length, character) ===> OOOOOOObananaOOOOOOO
txt = "banana"

x = txt.center(20, "O")

print(x)

# count()
txt = "banana"
print(txt.count("a"))
# Output: 3
# Counts how many times a substring appears in the string.
# Takes the value to count, with optional start and end indexes.

# encode()
txt = "hello"
print(txt.encode())
# Output: b'hello'
# Encodes the string into bytes using UTF-8 by default.
# Optional parameters include encoding type and error handling.

# endswith()
txt = "hello.txt"
print(txt.endswith(".txt"))
# Output: True
# Checks if the string ends with a specified value.
# You can also provide start and end positions.

# expandtabs()
txt = "a\tb\tc"
print(txt.expandtabs(4))
# Output: 'a   b   c'
# Replaces tab characters with spaces.
# The parameter sets the tab size.

# find()
txt = "hello world"
print(txt.find("world"))
# Output: 6
# Returns the index of the first occurrence of a value.
# Returns -1 if the value is not found.

# format()
txt = "My name is {}"
print(txt.format("Alex"))
# Output: 'My name is Alex'
# Inserts values into placeholders in a string.
# Parameters replace the {} placeholders in order or by name.

# format_map()
data = {"name": "Alex"}
print("My name is {name}".format_map(data))
# Output: 'My name is Alex'
# Formats a string using values from a dictionary.
# Takes a mapping object instead of positional arguments.

# index()
txt = "hello world"
print(txt.index("world"))
# Output: 6
# Returns the index of the first occurrence of a value.
# Raises an error if the value is not found.

# isalnum()
txt = "Hello123"
print(txt.isalnum())
# Output: True
# Checks if all characters are letters or numbers.
# Returns False if there are spaces or symbols.

# isalpha()
txt = "Hello"
print(txt.isalpha())
# Output: True
# Checks if all characters are alphabet letters.
# Numbers and spaces cause False.

# isascii()
txt = "Hello!"
print(txt.isascii())
# Output: True
# Checks if all characters are ASCII.
# Returns False for emojis or accented characters.

# isdecimal()
txt = "123"
print(txt.isdecimal())
# Output: True
# Checks if all characters are decimal numbers.
# Does not accept fractions or special numeric symbols.

# isdigit()
txt = "123"
print(txt.isdigit())
# Output: True
# Checks if all characters are digits.
# Accepts more digit characters than isdecimal().

# isidentifier()
txt = "variable_name"
print(txt.isidentifier())
# Output: True
# Checks if the string is a valid Python identifier.
# Cannot start with a number or contain spaces.

# islower()
txt = "hello"
print(txt.islower())
# Output: True
# Checks if all letters are lowercase.
# Non-letter characters are ignored.

# isnumeric()
txt = "Ⅻ"
print(txt.isnumeric())
# Output: True
# Checks if all characters are numeric.
# Includes fractions and Roman numerals.

# isprintable()
txt = "Hello\n"
print(txt.isprintable())
# Output: False
# Checks if all characters are printable.
# Newlines and tabs return False.

# isspace()
txt = "   "
print(txt.isspace())
# Output: True
# Checks if the string contains only whitespace.
# Spaces, tabs, and newlines count as whitespace.

# istitle()
txt = "Hello World"
print(txt.istitle())
# Output: True
# Checks if each word starts with a capital letter.
# Lowercase letters must follow the capitals.

# isupper()
txt = "HELLO"
print(txt.isupper())
# Output: True
# Checks if all letters are uppercase.
# Non-letter characters are ignored.

# join()
lst = ["a", "b", "c"]
print("-".join(lst))
# Output: 'a-b-c'
# Joins elements of an iterable into a single string.
# The string calling join() is used as the separator.

# ljust()
txt = "cat"
print(txt.ljust(10, "."))
# Output: 'cat.......'
# Left-justifies the string to a specified width.
# Optional parameter sets the fill character.

# lower()
txt = "HELLO"
print(txt.lower())
# Output: 'hello'
# Converts all characters to lowercase.
# Takes no parameters.

# lstrip()
txt = "   hello"
print(txt.lstrip())
# Output: 'hello'
# Removes whitespace from the left side of the string.
# You can specify which characters to remove.

# maketrans()
table = str.maketrans("abc", "123")
print(table)
# Output: {97: 49, 98: 50, 99: 51}
# Creates a translation table for use with translate().
# Parameters map characters to replacements.

# partition()
txt = "a-b-c"
print(txt.partition("-"))
# Output: ('a', '-', 'b-c')
# Splits the string into three parts at the first separator.
# Returns a tuple (before, separator, after).

# replace()
txt = "banana"
print(txt.replace("a", "o"))
# Output: 'bonono'
# Replaces occurrences of a value with another.
# Optional parameter limits the number of replacements.

# rfind()
txt = "banana"
print(txt.rfind("a"))
# Output: 5
# Finds the last occurrence of a value.
# Returns -1 if not found.

# rindex()
txt = "banana"
print(txt.rindex("a"))
# Output: 5
# Finds the last occurrence of a value.
# Raises an error if not found.

# rjust()
txt = "cat"
print(txt.rjust(10, "."))
# Output: '.......cat'
# Right-justifies the string to a specified width.
# Optional parameter sets the fill character.

# rpartition()
txt = "a-b-c"
print(txt.rpartition("-"))
# Output: ('a-b', '-', 'c')
# Splits the string into three parts at the last separator.
# Returns a tuple (before, separator, after).

# rsplit()
txt = "a,b,c"
print(txt.rsplit(",", 1))
# Output: ['a,b', 'c']
# Splits the string from the right.
# Optional parameter limits the number of splits.

# rstrip()
txt = "hello   "
print(txt.rstrip())
# Output: 'hello'
# Removes whitespace from the right side of the string.
# You can specify which characters to remove.

# split()
txt = "a,b,c"
print(txt.split(","))
# Output: ['a', 'b', 'c']
# Splits the string into a list.
# Separator and max splits are optional.

# splitlines()
txt = "a\nb\nc"
print(txt.splitlines())
# Output: ['a', 'b', 'c']
# Splits the string at line breaks.
# Optional parameter keeps line breaks.

# startswith()
txt = "hello.txt"
print(txt.startswith("hello"))
# Output: True
# Checks if the string starts with a specified value.
# You can include start and end positions.

# strip()
txt = "   hello   "
print(txt.strip())
# Output: 'hello'
# Removes whitespace from both sides of the string.
# You can specify which characters to remove.

# swapcase()
txt = "Hello World"
print(txt.swapcase())
# Output: 'hELLO wORLD'
# Swaps uppercase to lowercase and vice versa.
# Takes no parameters.

# title()
txt = "hello world"
print(txt.title())
# Output: 'Hello World'
# Capitalizes the first letter of each word.
# Words are split by non-letter characters.

# translate()
txt = "abc"
table = str.maketrans("abc", "123")
print(txt.translate(table))
# Output: '123'
# Replaces characters using a translation table.
# Table is usually created with maketrans().

# upper()
txt = "hello"
print(txt.upper())
# Output: 'HELLO'
# Converts all characters to uppercase.
# Takes no parameters.

# zfill()
txt = "42"
print(txt.zfill(5))
# Output: '00042'
# Pads the string with zeros on the left.
# Parameter specifies the total length.




















  






