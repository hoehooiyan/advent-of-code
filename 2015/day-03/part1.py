# --- Day 3: Perfectly Spherical Houses in a Vacuum - --

"""
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

"""
# Open the text file
input = open('input.txt')

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
    if move == '^':
        y += 1
        all_houses.append([x, y])
    elif move == 'v':
        y -= 1
        all_houses.append([x, y])
    elif move == '<':
        x -= 1
        all_houses.append([x, y])
    elif move == '>':
        x += 1
        all_houses.append([x, y])


for i in all_houses:
    if i not in visited_location:
        visited_location.append(i)

print(len(visited_location))
