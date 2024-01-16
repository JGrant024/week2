# Change maker
# Write a function that calculates how many bills and coins someone would receive as change.

# Write a function make_change that accepts two arguments:

# total_charge - the amount of money owed
# payment - the amount of money payed
# Return a 2-dimensional tuple whose values represent the bills and coins.

# Reminder from Wes Boss
# Calling back to this podcast transcript quote

# A tuple is a very scary sounding name for an array where you the length and the item types are known.

# Follow Up Reminder from Sean
# In Python:

# Tuples are ordered collections of objects enclosed in parentheses ()
# Each element within the tuple occupies a specific position starting at index 0
# Unlike lists, tuples can't be directly changed, aka "immutable"
# For example, consider the following tuple:

# # Example change tuple
# (
#   (3, 0, 1, 1, 0, 1),
#   (4, 1, 0, 2)
# )

# The first item represents the bills:

# 3 singles
# 0 fives
# 1 ten
# 1 twenty
# 0 fifties
# 1 hundred
# The second item represents the coins

# 4 pennies
# 1 nickel
# 0 dimes
# 2 quarters
# Your function make_change() will return a tuple that resembles the above example based on the values the user gives for payment and total_change.

# Hint: consider writing a small function to help produce the "bills" tuple and another function to help produce the "coins" tuple.

# Calculate the change value
# Write a value_of_change function that accepts a 2-dimensional tuple like the one returned by the make_change function.

# This function should calculate the monetary value specified by the tuple.

# For example, if the following tuple were passed to value_of_change

# (
#   (3, 0, 1, 1, 0, 1),
#   (4, 1, 0, 2)
# )

# It would return 133.59

# As before, consider writing helper functions to deal with the bills and the coins separately.