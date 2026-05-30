# === PYTHON FUNCTION RECAP ===
# FUNCTION: Reusable code that performs a specific task.
# VARIABLE: A named storage container holding a reference to data.
# OBJECT: The actual data stored in memory (e.g., strings, numbers, lists).
# PARAMETER: A placeholder variable defined inside a function to accept input.
# ARGUMENT: The actual, real value you pass into the function when calling it.

# ONE UNIFIED EXAMPLE:
user_name = "Hoang"  # 'user_name' is a variable; '"Hoang"' is a string object


def greet(name, sep=" - ", end="!\n"):  # 'name', 'sep', 'end' are parameters
    # '+' (concatenation) joins strings exactly as they are.
    # print() automatically inserts 'sep' between multiple arguments that have gaps.
    print("Welcome", name, "", sep=sep, end=end)
# The Comma is the Trigger: Every time Python sees a comma separating your inputs inside print(),
# it schedules one insertion of your sep string.

# CALLING THE FUNCTION:
# '"Welcome"', 'user_name', and '"..."' are the arguments passed into the slots.
greet(user_name, sep=" *** ", end="!!\n")  # Output: Welcome *** Hoang!!

# UNDERSTANDING print() KEYWORDS:
# *objects : Allows the function to accept any number of arguments (like "Welcome", name).
# sep      : Controls what character goes BETWEEN the arguments (Default is a space ' ').
# end      : Controls what character is printed at the very END (Default is newline '\n').

# For funsies:
# print("hello, \"friend\""), this is so you could print strings with quotes inside them

# What if you use defaults scenario?

# INSTANCE 1: Using ALL defaults
# greet("Hoang")
# What Python does step-by-step:
# name = "Hoang"
# sep is NOT provided -> uses default " - "
# end is NOT provided -> uses default "!\n"
# Output: Welcome - Hoang!

# INSTANCE 2: Overriding ONLY sep
# greet("Hoang", sep=" *** ")
# What Python does:
# name = "Hoang"
# sep = " *** " (overwritten)
# end = "!\n" (default used)
# Output: Welcome *** Hoang!

# INSTANCE 3: Overriding BOTH sep and end
# greet("Hoang", sep=" | ", end=" END\n")
# What Python does:
# name = "Hoang"
# sep = " | "
# end = " END\n"
# Output: Welcome | Hoang END


# SUMMARY:

# 1. Given my variable "user_name", Python stores a string object (Hoang) in it.

# 2. Python reads the 'def greet(...)' line and CREATES a function
#    named 'greet' in memory.

# 3. Line 12 is important as it sets the default parameters of the newly created greet function.
# If no value is given for them later, they will be automatically used. For this code purposes they are stored.

# 4. Now, Python reaches greet() on Line 20, where it is called.
# It evaluates the arguments --> user_name = Hoang, sep[seperator of objects] = ***, end = !!\n

# 5. The called function's arguments ("sep" and "end") override the defaulted parameters. (check line 12).

# 6. "Name" on line 15, references the string object "Hoang."

# Now Python runs the print() function.

# Something --------------------------------------------------------------------------------------------------------
# \n -> newline. Example: "Hello\nWorld" puts Hello and World on separate lines.
# \t -> tab. Example: "Name:\tAlice\nAge:\t25" (This sequence inserts a horizontal tab space.)
# \" -> quotation mark. Example: "He said, \"Hi\"" puts quotes inside a string.
# \\ -> backslash. Example: "C:\\Users" prints a single literal backslash.

# \n => Hello
#       World
# \t => Name:   Alice
#       Age:    25
# \" => He said, "Hi"
# \\ => C:\Users
