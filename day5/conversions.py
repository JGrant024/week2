# Celsius to Fahrenheit
# The formula to convert a temperature from Celsius to Fahrenheit is:

# F = (C * 9/5) + 32

# Write a function that takes a temperature in Celsius, converts it Fahrenheit, and returns the value.

# Fahrenheit to Celsius
# The formula to convert a temperature from Fahrenheit to Celsius is:

# C = (F - 32) * 5/9

# Write a function that takes a temperature in Fahrenheit, converts it to Celsius, and returns the value.åç



# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Examples
celsius_temperature = 25
converted_fahrenheit = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} degrees Celsius is {converted_fahrenheit:.2f} degrees Fahrenheit.")

fahrenheit_temperature = 77
converted_celsius = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} degrees Fahrenheit is {converted_celsius:.2f} degrees Celsius.")
