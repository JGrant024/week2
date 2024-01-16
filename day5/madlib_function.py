# Many of these will look familiar to exercises we did last week, but this time we're going to specifically write them using functions.

# Madlib function
# Write a function that accepts two arguments: a name and a subject.

# The function should return a String with the name and subject interpolated in.

# For example:

# madlib("Jenn", "science")
# # "Jenn's favorite subject is science."

# madlib("Jeff", "history")
# # "Jeff's favorite subject is history."

# Provide default arguments in case one or both are omitted.

def madlib(name="John", subject="math"):
    return f"{name}'s favorite subject is {subject}."

# Examples with default arguments
result1 = madlib()
result2 = madlib("Jenn")
result3 = madlib("Jeff", "history")

print(result1)
print(result2)
print(result3)
