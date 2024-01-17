# Imagine that you're running a hotel, and you want to keep track of guests by floor and room number.

# Start with the following dictionary:

# hotel = {
#     '1': {
#         '185': ['George Jefferson', 'Wheezy Jefferson'],
#     },
#     '2': {
#         '237': ['Jack Torrance', 'Wendy Torrance'],
#     },
#     '3': {
#         '333': ['Neo', 'Trinity', 'Morpheus']
#     }
# }

# Write a program that does the following:

# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# After checking in or out, display a list of all the occupants and their rooms.
# Level Up
# Do not allow anyone to check into a room that is already occupied!
# Do not allow checking out of a room that isn't occupied!


# resevations = input("Hello! Are you ready to check in or check out? ") 
# room_floor = input(" Please enter floor numnber, then a room number. ")
# checking_in = input("What is the number of occupants and their names? ")

def display_occupants():
    print("\nCurrent Occupants:")
    for floor, rooms in hotel.items():
        for room, occupants in rooms.items():
            print(f"Floor {floor}, Room {room}: {', '.join(occupants)}")

def check_in():
    floor = input("Enter floor number: ")
    room = input("Enter room number: ")
    occupants_count = int(input("Enter the number of occupants: "))
    occupants = [input(f"Enter name of occupant {i + 1}: ") for i in range(occupants_count)]

    if floor in hotel and room in hotel[floor]:
        hotel[floor][room].extend(occupants)
    else:
        hotel.setdefault(floor, {}).setdefault(room, []).extend(occupants)

    display_occupants()

def check_out():
    floor = input("Enter floor number: ")
    room = input("Enter room number: ")

    if floor in hotel and room in hotel[floor]:
        occupants = hotel[floor][room]
        del hotel[floor][room]
        display_occupants()
        print(f"\nChecked out: {', '.join(occupants)}")
    else:
        print("\nRoom not found.")

while True:
    print("\nHotel Management System:")
    print("1. Check-In")
    print("2. Check-Out")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, 3): ")

    if choice == '1':
        check_in()
    elif choice == '2':
        check_out()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")