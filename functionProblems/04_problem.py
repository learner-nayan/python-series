# METHOD ONE

# def area_and_circumference(radius):
#     return (22/7) * (radius**2), 2 * (22/7) * radius
#
# print(area_and_circumference(3))


# METHOD TWO

import math

def area_and_circumference(radius):
    return math.pi * radius ** 2, 2 * math.pi * radius


a, c = area_and_circumference(3)

print("Area:",round(a,2), "Circumference:",round(c,2))