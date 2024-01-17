# is_even function
# Write a function that accepts a number as an argument and returns a Boolean value. Return True if the number is even; return False if it is not even.

# is_odd function
# Write an is_odd function that uses your is_even function to determine if a number is odd. (That is, do not do the calculation - call a function that does the calculation.)

# Hint: You'll use the not keyword.

# only_evens function
# Write a function that accepts a List of numbers as an argument.

# Return a new List that includes the only the even numbers.

# only_evens([11, 20, 42, 97, 23, 10])
# # Returns [20, 42, 10]

# Hint: use your is_even() function to determine which numbers to include in your new List.

# only_odds function
# Write a function that accepts a List of numbers as an argument.

# Return a new List that includes the only the odd numbers.

# only_odds([11, 20, 42, 97, 23, 10])
# # Returns [11, 97, 23]

# Hint: use your is_odd() function to determine which numbers to include in your new List.

# is_even function
def is_even(number):
    return number % 2 == 0

# is_odd function using is_even with the not operator https://realpython.com/python-not-operator/#getting-started-with-pythons-not-operator
def is_odd(number):
    return not is_even(number)

# only_evens function
def only_evens(numbers):
    return [num for num in numbers if is_even(num)]

# only_odds function
def only_odds(numbers):
    return [num for num in numbers if is_odd(num)]

# Examples
numbers_list = [11, 20, 42, 97, 23, 10]

# Test only_evens function
even_numbers = only_evens(numbers_list)
print("Only Evens:", even_numbers)

# Test only_odds function==
odd_numbers = only_odds(numbers_list)
print("Only Odds:", odd_numbers)


# Other Examples: 

# numbers_list = [11, 20, 42, 97, 23, 10]
# for n in number_list: 
    # if is_odd(n): 
        # print(n)

num = input("please input a squence of numbers. ")

interger_list = [] 
for  n in interger_list: 
    if n != " ": 
        interger_list.append(int(n))
    print(interger_list)


for n in num: 
    if is_odd(n): 
        print(n) 