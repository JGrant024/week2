# # Go back to the Person class.

# # class Person:
# #     def __init__(self, name, email, phone):
# #          self.name = name
# #          self.email = email
# #          self.phone = phone

# #      def greet(self, other_person):
# #          print('Hello %s, I am %s!' % (other_person.name, self.name))

# # Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person.

# # sonny.print_contact_info()

# # Should generate this output:

# # Sonny's email: sonny@hotmail.com
# # Sonny's phone number: 483-485-4948




# Add an instance variable (attribute)
# Add a friends instance variable (attribute) to the Person class.

# You will initialize it to an empty list within the constructor __init__.

# Once you've done this you should be able to add a friend to a person using list's append method:

# jordan.friends.append(sonny) sonny.friends.append(jordan)

# You should also be able to get the number of friends a person has by using the len function on his friends:

# len(jordan.friends)

# Will return:

# 1

# Add an add_friend method
# The fact that a person's friends attribute is a list is an implementation detail of the Person class.

# Occassionally you'll want to hide implementation details from the users of your object/class. Implement an add_friend method to Person, so that in order to add a friend you call this method:

# jordan.add_friend(sonny)

# instead of:

# jordan.friends.append(sonny)

# Add a num_friends method
# We also want to hide the implementation detail that there is a friends attribute containing a list of friends.

# To do this, we'll implement a num_friends method which returns the number of friends for a person.

# For example:

# jordan.num_friends()
# 1