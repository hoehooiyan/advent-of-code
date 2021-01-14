# Day 1: Not Quite Lisp
# https://adventofcode.com/2015/day/1

# Read from the input file
with open("input.txt", "r") as fin:
    data = fin.read()

    # Convert a string of data into a list of instructions
    instructions = list(data)

    def final_position(instruction):
        santa_position = 0

        for i in instruction:
            if i == "(":
                santa_position += 1
            elif i == ")":
                santa_position -= 1

        print("Santa's final position: ", santa_position)

    final_position(instructions)
