# Day 1: Not Quite Lisp
# https://adventofcode.com/2015/day/1

# Open the text file
input_file = open("input.txt", "r")

# Read data from the text file
data = input_file.read()

# Close the text file
input_file.close()

# Convert a string of data into a list of instructions
instructions = list(data)


def final_position(instruction):
    santa_position = 0
    first_char = 1

    for i in instruction:
        if i == "(":
            santa_position += 1
        elif i == ")":
            santa_position -= 1
        if santa_position == -1:
            break

        first_char += 1

    print(
        "The position of the character causes Santa to first enter the basement: ",
        first_char,
    )


final_position(instructions)
