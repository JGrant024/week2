# Create a class Vehicle. A Vehicle object will have 3 attributes:

# make
# model
# year
# A vehicle is created like this:

# car = Vehicle('Nissan', 'Leaf', 2015)

# And you can access it's attributes individually like so:

# print(car.make, car.model, car.year)

# Add a method
# Add a print_info method to the Vehicle class. It will print out the vehicle's information like so:

# car.print_info()

# Will output:

# 2015 Nissan Leaf

class Vehicle: 
    def __init__(self, year, make, model,): 
        self.year = year
        self.make = make 
        self.model = model
    
    def print_info(self): 
        print("%s %s %s" % (self.year, self.make, self.model))

car = Vehicle('2022', 'Honda', 'Piolot')

car.print_info()
