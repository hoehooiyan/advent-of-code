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

final_location = [0, 0]
x = final_location[0]
y = final_location[1]
all_houses = []
visited_location = [[0, 0]]


for move in new_moves:
    if move == "^":
        y += 1
        all_houses.append([x, y])
    elif move == "v":
        y -= 1
        all_houses.append([x, y])
    elif move == "<":
        x -= 1
        all_houses.append([x, y])
    elif move == ">":
        x += 1
        all_houses.append([x, y])


for i in all_houses:
    if i not in visited_location:
        visited_location.append(i)

print(len(visited_location))
