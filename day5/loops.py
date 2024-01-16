# Start/End
# Ask the user for a starting number, assign it to a variable.
# Ask the user for an ending number, assign it to a variable.
# Write a loop that increments the starting number by 1 until it matches the ending number.
# Bonus
# Can you write a loop that increments by more than 1?
# Can you create a range of numbers from which the user can choose?
# Can you let the user know when they choose something out of that range?

#creates a variable that asks the user for their starting number. 
start_number = int(input("What is your starting number? "))


#creates a varibale that asks for the user for their ending number. 
end_number = int(input("What is your ending number? ")) 


#created a while loop that reads while the start number is less than the ending number displays the current number and its value adding 1 to each line iterated over. 
while start_number < end_number: 
        print("Current number", start_number)
        start_number += 1 
print("Loop completed! ")