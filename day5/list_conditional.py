# Make a new list containing members of your favorite band/sports team/television show.
# Write a conditional statement to check if a specific person is in that list.
# If they are in the list, remove them.
# If they're not in the list, add them.
# Can you write a condition that does both of these checks?

# Think like this: "If the person exists, then remove them. Otherwise, if they don't, add them.\
# Print the updated list. 

# Make a new list containing members of your favorite band/sports team/television show.
favorite_players = ["Kobe Bryant", "Jonathan Grant", "Michael Jordan"]

# Person to check
person_to_check = "Michael Jordan"

# created conditional statements using if else to check if players are in the list, and how to add and remove them from list. 
if person_to_check in favorite_players:
    # If they are in the list, remove them.
    favorite_players.remove(person_to_check)
else:
    # If they're not in the list, add them.
    favorite_players.append(person_to_check)

# Print the updated list, passing in favorite_players as arguement 
print("Updated List:", favorite_players)
