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


def surface_area(dimensions):
    """Find the surface area of the box.

    l: length
    w: width
    h: height
    """
    total = 0

    for item in dimensions:
        after_splitting = item.split("x")

        l = int(after_splitting[0])
        w = int(after_splitting[1])
        h = int(after_splitting[2])

        result = (2 * l * w) + (2 * w * h) + (2 * h * l)

        total += result

    return total


def smallest_area(dimensions):
    """Find the smallest area of the box.

    x: short length 1 (could be l or w or h)
    y: short length 2 (could be l or w or h)
    """
    area = 0
    total = 0

    for item in dimensions:
        after_splitting = item.split("x")

        l = int(after_splitting[0])
        w = int(after_splitting[1])
        h = int(after_splitting[2])

        max_num = max(l, w, h)

        if l == max_num:
            area = w * h
        elif w == max_num:
            area = l * h
        elif h == max_num:
            area = l * w

        total += area

    return total


total1 = surface_area(new_dimensions)
total2 = smallest_area(new_dimensions)
total_square_feet = total1 + total2

print(total_square_feet)
