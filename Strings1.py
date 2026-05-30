# Ask user for their name
name = input("What's your name? ")

# Print a greeting using print() parameters
print("Hello", name, sep=", ", end="!")
# What's your name? Hoang
# Hello, Hoang!

# This is one of the many examples of string concatenation.
# The greeting Hello is being combined with the inputted name.
# It also has a seperator, a keyword parameter that controls the spacing as it has a space after
# a comma. Finally, the phrase ends with the exclamation mark, which replaces the default \n
# which creates a new line.

# Knowing how Python functions work is pretty useful, so we usually look into their documentation.
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# Remember, you use commas to pass multiple objects between the same lines,
# and the seperator keyword to define what appears between them.

### Some common ways of string joining:

## 1. Using separate arguments (default print behavior)
 # print("hello", "world")

## 2. Using sep parameter
 # print("hello", "world", sep=" ")

## 3. Using string concatenation
 # print("hello" + " " + "world")

## 4. Using f-string
 # print(f"hello world")

## 5. Using end parameter with two print statements
 # print("hello", end=" ")
 # print("world")