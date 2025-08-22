""" 
Python-Project
2025-08-21
Robot Challenge
"""
# Game name
print("--------------------")
print("Robot Game Simulator")
print("--------------------\n")

# Welcom the player
player = input("What is your name?: ")
print(f"Welcome {player}!\n")

# Prompt the player to name the robot
name = input("ENTER a name for the robot: ")

# Print the input
print(f"Your ROBOT's name is: {name}\n")

# Robot must have 4 hitpoints
hitpoints = 4

# Robot will start in the corner of a grid
position = [0, 0]

# The grid will be a 4 x 4 grid
# Enter obstacles coordinates
obstacles = [(1, 1), (2, 2), (2, 3), (4,1)]

print(f"{player} - The rules are simple: Don't let {name} hit any obstacles!")

 # Make it more interactive
print("\nAre You READY?")
input("\nPress any key to continue.\n")

# Instructions Breakdown
print("***************************************************************************")
print(f"\nTake note of the following commands to navigate {name} through the 4x4 grid:\n")
print("***************************************************************************\n")
print("1: u = up")
print("2: d = down")
print("3: l = left")
print("4: r = right")
print(f"\nUse 'u', 'd', 'l' and 'r' to navigate {name} across the map.\n")

 # Make it more interactive
input("\nPress any key to continue.\n\n")

# START THE GAME
while hitpoints > 0:
    print(f"{name}'s coordinates on the grid are: {position}")
    print(f"{name} has a total of {hitpoints} hitpoints left.\n")

# Prompt for the command
    command = input(f"----> Give {name} the next command (u / d / l / r): ")

# Implement commands and movement for the Robot
    if command == "l":
            print(f"\n*** You entered 'l' to move {name} one space left. ***\n")
            position[0] -= 1
    elif command == "r":
            print(f"\n*** You entered 'r' to move {name} one space right. ***\n")
            position[0] += 1
    elif command == "u":
            print(f"\n*** You entered 'u' to move {name} one space up. ***\n")
            position[1] += 1
    elif command == "d":
            print(f"\n*** You entered 'd' to move {name} one space down. ***\n")
            position[1] -= 1
    else:
            print(f"\n*** Incorrect input. You can only use 'u', 'd', 'l' and 'r' to move {name}. ***\n")

# CHECK Boundary Box
    if position [0] < 0 or position [0] > 4 or position[1] < 0 or position[1] > 4:
            print("***************************************************************************")
            print("Out of Bounds! Please stay within the 4 x 4 grid.")
            print("***************************************************************************\n")

# REVERSE movement for the Robot
            if command == "l":
                position[0] += 1
            elif command == "r":
                position[0] -= 1
            elif command == "u":
                position[1] -= 1
            elif command == "d":
                position[1] += 1

# Obstacle detection                
    if (position [0], position [1]) in obstacles:
        hitpoints -= 1
        print(f"WATCH OUT!\n{name} hit an obstacle and lost 1 hitpoint.")
        print(f"{name} should try a different route instead.\n")

# REVERSE movement for the Robot
        if command == "l":
            position[0] += 1
        elif command == "r":
            position[0] -= 1
        elif command == "u":
            position[1] -= 1
        elif command == "d":
            position[1] += 1

        if hitpoints == 0:
            print(f"Oh dear! {name} died!")
            break
        
# End of game
print("\nGoodbye.\n\n\n")