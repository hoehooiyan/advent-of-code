# Day 3: Perfectly Spherical Houses in a Vacuum
# https://adventofcode.com/2015/day/3

with open("input.txt", "r") as fin:
    data = fin.read()
    moves = list(data)  # Convert str to list
    new_moves = moves[:-1]  # Get the last move

    x, y = starting_location = [0, 0]
    all_houses = []
    visited_location = [starting_location]

    def add_house(coordinate_x, coordinate_y):
        all_houses.append([coordinate_x, coordinate_y])

    for move in new_moves:
        if move == "^":
            y += 1
            add_house(x, y)
        elif move == "v":
            y -= 1
            add_house(x, y)
        elif move == "<":
            x -= 1
            add_house(x, y)
        elif move == ">":
            x += 1
            add_house(x, y)

    for i in all_houses:
        if i not in visited_location:
            visited_location.append(i)

    print(len(visited_location))
