# Make a string with at least 6 characters.
# Make an empty list (hint: create a variable with no value between the brackets)
# Loop through each letter in your string and for each letter in the string, append it to the empty list.
# Revese the list.
# Create a new variable that is an empty string (just like in JavaScript).
# Loop through the list, for each letter in the list, add it to the new string your created.
# Print out the new string. It should be the reversed version of the string you created. i.e. "sean" -> "neas".

#Created a string with at least 6 characters
string_name = "coding"

#empty list 
empty_list = [] 

# for loop that iterates over each letter in the string 
for letter in string_name:
    empty_list.append(letter) 


#reverses list 
empty_list.reverse() 

#empty string 
empty_string = ""


#for loop that iterates over each element in the list
for letter in empty_list:   
    empty_string += letter 


print("Reversed String",empty_string)

