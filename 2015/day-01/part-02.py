# ---Day 1: Not Quite Lisp---

"""PART 2

Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?

"""

# Open the text file
input_file = open('input.txt', 'r')

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
        if i == '(':
            santa_position += 1
        elif i == ')':
            santa_position -= 1
        if santa_position == -1:
            break

        first_char += 1

    print('The position of the character causes Santa to first enter the basement: ', first_char)


final_position(instructions)
