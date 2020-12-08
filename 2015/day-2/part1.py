# --- Day 2: I Was Told There Would Be No Math - --

"""
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions(length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box(a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?


1. What is a right rectangular prism?
2. What is the formula of finding the surface area? (2*l*w + 2*w*h + 2*h*l)
3. How to find the area of the smallest side?
"""

# Open the text file
input = open('input.txt')

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
        after_splitting = item.split('x')

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
        after_splitting = item.split('x')

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
