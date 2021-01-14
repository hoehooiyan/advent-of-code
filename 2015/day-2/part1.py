# Day 2: I Was Told There Would Be No Math
# https://adventofcode.com/2015/day/2

with open("input.txt", "r") as fin:
    dimensions = []

    for line in fin:
        data = line.strip()
        dimensions.append(data)

    def get_single_value(combined_values):
        after_splitting = combined_values.split("x")

        l = int(after_splitting[0])
        w = int(after_splitting[1])
        h = int(after_splitting[2])

        return (l, w, h)

    def surface_area(dimensions):
        """Find the surface area of the box.

        l: length
        w: width
        h: height
        """
        total = 0

        for item in dimensions:
            l, w, h = get_single_value(item)
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
            l, w, h = get_single_value(item)
            max_num = max(l, w, h)

            if l == max_num:
                area = w * h
            elif w == max_num:
                area = l * h
            elif h == max_num:
                area = l * w

            total += area
        return total

    total1 = surface_area(dimensions)
    total2 = smallest_area(dimensions)
    total_square_feet = total1 + total2

    print(total_square_feet)
