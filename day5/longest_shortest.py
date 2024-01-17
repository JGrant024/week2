# Find the shortest String
# Write a function shortest that accepts a List of Strings as an argument.

# It should return the shortest String in the List.

# Find the longest String
# Write a function longest that accepts a List of Strings as an argument.

# It should return the longest String in the List.

# Find the smallest number
def smallest(numbers):
    if not numbers:
        return None  # Return None for an empty list
    return min(numbers)

# Find the largest number
def largest(numbers):
    if not numbers:
        return None  # Return None for an empty list
    return max(numbers)

# Examples
numbers_list = [11, 20, 42, 97, 23, 10]

# Test smallest function
smallest_num = smallest(numbers_list)
print("Smallest Number:", smallest_num)

# Test largest function
largest_num = largest(numbers_list)
print("Largest Number:", largest_num)
