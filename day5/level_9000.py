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




                                         #step 1.) find the difference between the amount total, and the amount paid. 
                                         #step 2.) Split the difference into bills and coins 
                                         #step 3.) Create or call the functions (run the other functions count_bills, count_coins ) 
                                         #step 4.) That the result of those two functions and return a tuple. 
     
def make_change(total_charge, payment):
    #find the difference 
    difference = payment - total_charge
    #Split the difference into bills and coins 

    difference_as_string = str(difference)
    parts = difference_as_string.split(".")
    #Define the bills and coins bacsed on the parts
    bills = parts[0]
    coins = parts[1]
    return count_bills(bills), count_coins(coins)

def count_bills(payment_in_bills):
    payment_in_bills = int(payment_in_bills)

    hundreds = payment_in_bills //100 
    payment_in_bills %= 100 

    fifties = payment_in_bills //50
    payment_in_bills %= 50

    twenties  = payment_in_bills //20
    payment_in_bills %= 20

    tens = payment_in_bills //10
    payment_in_bills %= 10

    fives = payment_in_bills //5
    payment_in_bills %= 5 

    singles = payment_in_bills //1
    payment_in_bills %= 1
    return(singles, fives, tens, twenties, fifties, hundreds)
    

def count_coins(payment_in_coins):
    payment_in_coins = int(payment_in_coins)

    quarters = payment_in_coins// 25
    payment_in_coins %= 25

    dimes = payment_in_coins// 10
    payment_in_coins %= 10

    nickels  = payment_in_coins// 5
    payment_in_coins %= 5

    pennies = payment_in_coins// 1
    payment_in_coins %= 1
    return (quarters, dimes, nickels, pennies)


# you can turn predicatable inputs into a function 
print(make_change(148.49, 200)) 