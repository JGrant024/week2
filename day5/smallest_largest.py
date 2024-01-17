# Find the smallest number
# Write a function smallest that accepts a List of numbers as an argument.

# It should return the smallest number in the List.

# Find the largest number
# Write a function largest that accepts a List of numbers as an argument.

# It should return the largest number in the List.



# Find the smallest number
def smallest(numbers):
    if not numbers:
        return None  # Return None for an empty list
    smallest_num = numbers[0]  # Assume the first number is the smallest
    for num in numbers[1:]:
        if num < smallest_num:
            smallest_num = num
    return smallest_num

# Find the largest number
def largest(numbers):
    if not numbers:
        return None  # Return None for an empty list
    largest_num = numbers[0]  # Assume the first number is the largest
    for num in numbers[1:]:
        if num > largest_num:
            largest_num = num
    return largest_num

# Examples
numbers_list = [11, 20, 42, 97, 23, 10]

# Test smallest function
smallest_num = smallest(numbers_list)
print("Smallest Number:", smallest_num)

# Test largest function
largest_num = largest(numbers_list)
print("Largest Number:", largest_num)
