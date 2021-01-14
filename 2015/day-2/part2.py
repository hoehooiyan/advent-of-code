# Day 2: I Was Told There Would Be No Math
# https://adventofcode.com/2015/day/2

# Open the text file
input = open("input.txt")

# Read data from the text file
data = input.readlines()

# Close the text file
input.close()

# Convert the data into a list of dimensions
dimensions = list(data)

# New dimension list
new_dimensions = [i[:-1] for i in dimensions]


def perimeter(x, y):
    return x + x + y + y


def total_perimeter(dimensions):
    total = 0

    for item in dimensions:
        after_splitting = item.split("x")

        l = int(after_splitting[0])
        w = int(after_splitting[1])
        h = int(after_splitting[2])

        max_num = max(l, w, h)

        if l == max_num:
            p = perimeter(w, h)
        elif w == max_num:
            p = perimeter(l, h)
        elif h == max_num:
            p = perimeter(l, w)

        total += p

    return total


def volume(dimensions):
    total = 0

    for item in dimensions:
        after_splitting = item.split("x")

        l = int(after_splitting[0])
        w = int(after_splitting[1])
        h = int(after_splitting[2])

        result = l * w * h

        total += result

    return total


total1 = total_perimeter(new_dimensions)
total2 = volume(new_dimensions)
total_feet_ribbon = total1 + total2

print(total_feet_ribbon)
