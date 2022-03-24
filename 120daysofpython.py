# Coding Room Exercises

#-----------------------------------------------------------------------------

# DAY 001

#-----------------------------------------------------------------------------

# SHORTCUT: ctrl + 1 = add comment

# 1. Printing
# Write a program in main.py that prints the same notes from the previous lesson 
# using what you have learnt about the Python print function.

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#-----------------------------------------------------------------------------

# 2. Debugging Practice
# There are errors in all of the lines of code. 
# Fix the code so that it runs without errors.

# a. Missing double quotes before the word Day.
print("Day 1 - String Manipulation")

# b. Outer double quotes changed to single quotes.
print('String Concatenation is done with the "+" sign.')

# c. Extra indentation removed
print('e.g. print("Hello " + "world")')

# d. Extra ( in print function removed.
print("New lines can be created with a backslash and n.")

#-----------------------------------------------------------------------------

# 3. Input Function
# Write a program that prints the number of characters in a user's name.

print(len(input("What is your name?\n")))

# example:
# len(number of characters)
# if input was "Jack".
# 1st: print(len("Jack"))
# 2nd: print(4)

#-----------------------------------------------------------------------------

# 4. Variables
# Write a program that switches the values stored in the variables a and b.
# 🚨 Don't change the code below 👇

a = input("a: ")
b = input("b: ")

#-----------------------------------
#Write your code below this line 👇

c = a
a = b
b = c

#-----------------------------------
# 🚨 Don't change the code below 👇

print("a: " + a)
print("b: " + b)

# note: Pay attention to the order of the code in this scenario.

#-----------------------------------------------------------------------------

# DAY 002

#-----------------------------------------------------------------------------

# 1. Data Types
# Write a program that adds the digits in a 2 digit number. 
# E.g. if the input was 35, then the output should be 3 + 5 = 8.
