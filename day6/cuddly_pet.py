# Start with these classes:

# class Pet:
#     def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
#         self.name = name
#         self.fullness = fullness
#         self.happiness = happiness
#         self.hunger = hunger
#         self.mopiness = mopiness

#     def eat_food(self):
#         self.fullness += 30

#     def get_love(self):
#         self.happiness += 30

#     def be_alive(self):
#         self.fullness -= self.hunger
#         self.happiness -= self.mopiness


# class CuddlyPet(Pet):
#     def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
#         super().__init__(name, fullness, 100, hunger, 1)
#         self.cuddle_level = cuddle_level

#     def be_alive(self):
#         self.fullness -= self.hunger
#         self.happiness -= self.mopiness/2

#     def cuddle(self, other_pet):
#         # Super cuddle powers, activate!
#         for i in range(self.cuddle_level):
#             other_pet.get_love()


# Level 1
# Overriding __str__() in CuddlyPet

# When you pass a CuddlyPet instance to the print() function, it uses the Pet version of the method.

# Override the definition of __str__() in CuddlyPet so that the return value includes the string "Extra cuddly".

# Using super() in CuddlyPet.be_alive()

# CuddlyPet has a custom version of be_alive(), but it's nearly identical to the definition in Pet. The only difference is that we subtract self.mopiness/2 from self.happiness for a CuddlyPet.

# If our Virtual Pets get more complex, we might add more lines to be_alive(). It would be tedious to update both versions of be_alive().

# One solution is for CuddlyPet to call Pet.be_alive() and then increase its self.happiness. Modify CuddlyPet.be_alive() so that it calls super() to invoke Pet's version of be_alive().

# Level 2
# Add a Treat class to your Pet simulator.

# When you give one of your Pet objects a treat, prompt the user to choose one of three kinds:

# ColdPizza
# Bacon
# VeganSnack
# Create a class for each of these, and customize them so that they have differing effects on the Pet object's fullness and happiness levels.

# Create a Menu class for your Pet simulator

# Create a Menu class that has the following attributes:

# prompt_text - the text to show the user
# Add the following methods to the Menu class

# get_choice() - shows the user the prompt_text and converts their input to an int, prompting again if they enter an invalid value.
# Modify the while loop of your Pet simulator so that it uses a Menu instance to handle user interaction. For each additional prompt (such as choosing which kind of Pet subclass to adopt), use additional Menu instances.