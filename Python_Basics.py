#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:50:41 2018

@author: ditapeskova
"""

# Python Basics

# Basic Calculations

# Addition and subtraction
print(10 + 3)
print(20 - 14)

# Multiplication and division
print(7 * 6)
print(21 / 7)

# Exponentiation
print(6 ** 2)

# Modulo
print(53 % 8)


# Variables
# Case sensitive, specific
# Can be called up later through variable name

distance = 300
time = 20
speed = distance / time
speed


#Check Type of Variable
type(speed)

z = True
type(z)

# Converting Types Of Variables
# Converting Float to String

investment = 1000
earnings = 120

text = ("I have invested" + str(investment) + "$ and earned" + str(earnings)+"$")
print(text)
type(text)

# Converting String to Float

result = "4.57685"

number = float(result)
print(result)

type(number)


# Lists
# Can contain elements of any type in one list
# Lists are created with []

weight = ["jane", 65, "peter", 72, "kate", 59, "leon", 85]

# Lists can contain other lists
weight_all = [["jane", 65],
              ["peter", 72],
              ["kate", 59],
              ["leon", 85]]

type(weight)
type(weight_all)

# Selecting Elements From Lists
# Use name of list and index number of element you are selscting
# Python index starts from 0

# Selecting "peter" from weight list
weight[2]

# Negative indices
# Used to get elements at the end of the list
# Negative index starts from -1 from the last element

# Choose "kate" from the list
weight[-4]

# List Slicing
# Allows you to choose multiple elements from the list
# Use colon symbol

# Selecting "peter", 73, "kate" and 59
# Remeber: element after a colon is excluded
# to end selection with 5th element you need to select 6

weight[2:6]

# To start with first element leave out index before the colon
weight[:4]

# To end with last element leave out index after the colon
weight[3:]

# Adding list selections
# Have to be same type

weight_total = weight[1] + weight[3] + weight [5] + weight [7]
print(weight_total)

# Changing elements in lists
# Use [] for element you are changing

# Changing 65 to 72 in weight list
weight[1] = 72
weight

# Changing "peter", 72 to "richard", 78
weight[2:4] = "richard", 78
weight

# Adding elements to the lists
# Adding "frank", 82 to the list
weight_add = weight + ["frank", 82]
weight_add

# Deleting element fro mthe list
# Deleting "kate", 59 from the weight_add list
del(weight_add[4:6])
weight_add

# Copying list to prevent changes in original list
weight_copy = list(weight)
weight_copy[3] = 92
print(weight)
print(weight_copy)












