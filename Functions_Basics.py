#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:42:28 2018

@author: ditapeskova
"""

# Functions
# Structure of Simple Function
# output = function_name(input)

# Finding max value of a list
expenses = [3.21, 67.76, 87.64, 54, 6.1, 78.4]
max(expenses)

# Round number
round(1.34)

# Round number of one decimal place
round(1.34, 1)

# Finding out lenght of a list
len(expenses)

# Create a complex number
complex(2)

# Finding more about functions
# Finding arguments that can be entered
# Argument in [] is an optional argument
help(round)

# Sorting list in ascending order
sorted(expenses, reverse = False)

# Sorting list in descending order
sorted(expenses, reverse = True)

# Methods
# Methods are functions that belong to specific objects

# List Methods

cont = ["jane", 124, "peter", 157, "ben", 48, "frank", 203, "mandy", 95]

# Get index of an element
cont.index("ben")

# How many times an element appears in a list
cont.count(124)

# Add one element at the end of a list
cont.append("kate")
cont.append(143)

# Reverse the order of the elements in the list it is called on
expenses.reverse()

# Remove the first element of a list that matches the input
expenses.remove(6.1)


# String Methods

cat = "pepper"

# Capitalize first letter
cat.capitalize()

# Replace parts of a string (pepper to pepps)
cat.replace("er","s")

# Capitalize all the letters
cat.upper()

# Find out all the methods for string
help(str)







