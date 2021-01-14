# Day 3: Perfectly Spherical Houses in a Vacuum
# https://adventofcode.com/2015/day/3

with open("input.txt", "r") as fin:
    data = fin.read()
    moves = list(data)  # Convert str to list
    new_moves = moves[:-1]  # Get the last move

    x, y = starting_location = [0, 0]
    all_houses = []
    visited_location = [starting_location]

    # Starting location of santa
    santa_x, santa_y = starting_location
    # Starting location of robo
    robo_x, robo_y = starting_location

    all_houses = []
    visited_location = [starting_location]

    def add_house(coordinate_x, coordinate_y):
        all_houses.append([coordinate_x, coordinate_y])

    # Santa's moves
    for i in range(0, len(new_moves), 2):
        if new_moves[i] == "^":
            santa_y += 1
            add_house(santa_x, santa_y)
        elif new_moves[i] == "v":
            santa_y -= 1
            add_house(santa_x, santa_y)
        elif new_moves[i] == "<":
            santa_x -= 1
            add_house(santa_x, santa_y)
        elif new_moves[i] == ">":
            santa_x += 1
            add_house(santa_x, santa_y)

    # Robo-Santa's moves
    for i in range(1, len(new_moves), 2):
        if new_moves[i] == "^":
            robo_y += 1
            add_house(robo_x, robo_y)
        elif new_moves[i] == "v":
            robo_y -= 1
            add_house(robo_x, robo_y)
        elif new_moves[i] == "<":
            robo_x -= 1
            add_house(robo_x, robo_y)
        elif new_moves[i] == ">":
            robo_x += 1
            add_house(robo_x, robo_y)

    for i in all_houses:
        if i not in visited_location:
            visited_location.append(i)

    print(len(visited_location))
