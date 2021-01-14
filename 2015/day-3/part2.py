# Day 3: Perfectly Spherical Houses in a Vacuum
# https://adventofcode.com/2015/day/3

# Open the text file
input = open("input.txt")

# Read data from the text file
data = input.read()

# Close the text file
input.close()

# Convert the data into a list
moves = list(data)
new_moves = moves[:-1]

# Starting location of santa
santa = [0, 0]
santa_x = santa[0]
santa_y = santa[1]

# Starting location of robo_santa
robo_santa = [0, 0]
robo_x = robo_santa[0]
robo_y = robo_santa[1]

all_houses = []
visited_location = [[0, 0]]

# Santa's moves
for i in range(0, len(new_moves), 2):
    if new_moves[i] == "^":
        santa_y += 1
        all_houses.append([santa_x, santa_y])
    elif new_moves[i] == "v":
        santa_y -= 1
        all_houses.append([santa_x, santa_y])
    elif new_moves[i] == "<":
        santa_x -= 1
        all_houses.append([santa_x, santa_y])
    elif new_moves[i] == ">":
        santa_x += 1
        all_houses.append([santa_x, santa_y])


# Robo-Santa's moves
for i in range(1, len(new_moves), 2):
    if new_moves[i] == "^":
        robo_y += 1
        all_houses.append([robo_x, robo_y])
    elif new_moves[i] == "v":
        robo_y -= 1
        all_houses.append([robo_x, robo_y])
    elif new_moves[i] == "<":
        robo_x -= 1
        all_houses.append([robo_x, robo_y])
    elif new_moves[i] == ">":
        robo_x += 1
        all_houses.append([robo_x, robo_y])

for i in all_houses:
    if i not in visited_location:
        visited_location.append(i)

print(len(visited_location))
