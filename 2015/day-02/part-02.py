# --- Day 2: I Was Told There Would Be No Math - --

"""
The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

How many total feet of ribbon should they order?
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


def perimeter(x, y):
    return x + x + y + y


def total_perimeter(dimensions):
    total = 0

    for item in dimensions:
        after_splitting = item.split('x')

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
        after_splitting = item.split('x')

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
