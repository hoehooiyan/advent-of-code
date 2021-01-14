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

    def perimeter(x, y):
        return x + x + y + y

    def total_perimeter(dimensions):
        total = 0

        for item in dimensions:
            l, w, h = get_single_value(item)
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
            l, w, h = get_single_value(item)
            result = l * w * h
            total += result
        return total

    total1 = total_perimeter(dimensions)
    total2 = volume(dimensions)
    total_feet_ribbon = total1 + total2

    print(total_feet_ribbon)
