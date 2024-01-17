# You may notice that when you are working with a person object, it's representation in the Python shell is pretty cryptic and unhelpful:

# >>> print(jordan)
# <__main__.Person object at 0x106976410>

# Adding the __str__ method to the Person class and have it return a string. Whatever you return there will be used to "represent" your person object.

# For example, say I want a Person to be represented like this: Jordan jordan@aol.com 495-586-3456

# I could implement str like this:

# def __str__(self):
#      return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

# Implement your own __str__ method, and you can represent your person objects however you want. Incidentally, __str__ is also used when you use convert your object to a string: i.e. str(jordan).