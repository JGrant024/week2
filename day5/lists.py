# Change a List

# Use the following list: numbers = [1, 2, 3, 4, 5, 99, 2600, 300]
# There is a Python method that will reverse a list.
# Create a new variable called reversed_list and assign it the reversed value of numbers.
# Print the values of each list.


# This creates a function that passes through the arguments of lst (short for list) then using the .reverse method and then to return the list. 
def reversed_list_method(lst): 
    lst.reverse() 
    return lst  

# number list from the example: 
number_list =[1, 2, 3, 4, 5, 99, 2600, 300] 

#created a variable reverse_list_method then used the .copy method to create a shollow copy of the list. Doc from "https://docs.python.org/3/library/copy.html"
reversed_list_method = reversed_list_method(number_list.copy())


#This will print the shollow copy of the number list, and then will create and print a reversed copy of the list using the reverse method. 
print("number list", number_list) 
print("reversed list (using the reverse method)", reversed_list_method)