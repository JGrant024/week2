# You may notice that when you are working with a person object,
# it's representation in the Python shell is pretty cryptic and unhelpful:

# >>> print(jordan)
# <__main__.Person object at 0x106976410>

# Adding the __str__ method to the Person class and have it return a string. 
# Whatever you return there will be used to "represent" your person object.

# For example, say I want a Person to be represented like this: 
# Jordan jordan@aol.com 495-586-3456

# I could implement str like this:

# def __str__(self):
#      return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

# Implement your own __str__ method, and you can represent your person objects however you want. Incidentally, __str__ is also used when you use convert your object to a string: i.e. str(jordan).

class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []

    def greet(self, other_person):
         print('Hello %s, I am %s!' % (other_person.name, self.name))


    # MAKE SURE YOU PASS IN EACH STRING TO COMPLETE ARGUMENTS! ex. ("%s" % (self.ex1, self.ex2))
    def print_contact_info(self):
       print("%s's Email: %s " %(self.name, self.email))
       print("%s's Phone Number: %s " % (self.name, self.phone))

# function that adds friends 
    def add_friend(self, friend): 
       self.friends.append(friend)

# a function that returns the legnth of friends
    def num_friends(self):
        return len(self.friends)
# a function that 
    def __str__(self):
        return "%s, %s, %s" % (self.name, self.email, self.phone)
    
jordan = Person("jordan", "jordan@aol.com", "495-586-3456")

print(jordan)