""" 
Python-Project
2025-08-21
Robot Challenge
"""

print("Robot Game Simulator")
print("--------------------\n")

# Prompt the player to name the robot
name = input("ENTER a name for the robot: ")

# Print the input
print(f"Your ROBOT's name is: {name}\n")

# Robot must have 4 hitpoints
hitpoints = 4

# Robot will start in the corner of a grid
position = [0, 0]

# The grid will be a 4 x 4 grid
# Enter Random obstacles
obstacles = [(1, 1), (2, 2), (2, 3), (4,1)]

print("***************************************************************************\n")
print(f"Welcome Player! The rules are simple: Don't let {name} hit any obstacles!\n")
print(f"Take note of the following commands to navigate {name} through the 4x4 grid:")
print("1: u = up")
print("2: d = down")
print("3: l = left")
print("4: r = right")
print(f"\nUse 'u', 'd', 'l' and 'r' to navigate {name} across the map.\n")
print("***************************************************************************\n")

# START THE GAME
while hitpoints > 0:
    print(f"{name}'s coordinates on the grid are: {position}")
    print(f"{name} has a total of {hitpoints} hitpoints left.\n")

# Prompt for the command
    command = input("\n----------> Enter a command (u / d / l / r): ")

# Implement commands and movement for the Robot
    if command == "l":
            print("\n\nYou entered 'l' to move left.\n")
            position[0] -= 1
    elif command == "r":
            print("\n\nYou entered 'r' to move right.\n")
            position[0] += 1
    elif command == "u":
            print("\n\nYou entered 'u' to move up.\n")
            position[1] += 1
    elif command == "d":
            print("\n\nYou entered 'd' to move down.\n")
            position[1] -= 1
    else:
            print(f"\n\nIncorrect input. You can only use 'u', 'd', 'l' and 'r' to move {name}\n")

# CHECK Boundary Box
    if position [0] < 0 or position [0] > 4 or position[1] < 0 or position[1] > 4:
            print("*****************************************************")
            print("Out of Bounds! Please stay within the 4 x 4 grid.")
            print("*****************************************************\n")

# REVERSE movement for the Robot
            if command == "l":
                position[0] += 1
            elif command == "r":
                position[0] -= 1
            elif command == "u":
                position[1] -= 1
            elif command == "d":
                position[1] += 1





