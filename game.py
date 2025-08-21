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

print(f"Welcome Player! The rules are simple: Don't let {name} hit any obstacles!\n")
print(f"Take note of the following commands to navigate {name} through the map:")
print("1: f = forward")
print("2: b = backward")
print("3: l = left")
print("4: r = right")
print(f"Use 'f', 'b', 'l' and 'r' to navigate {name} across the map.")