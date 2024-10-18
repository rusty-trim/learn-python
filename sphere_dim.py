# sphere_dim.py
#   A program that calculates the volume and area of a sphere by the given radius.

import math

def main():
    radius = float(input("What is the radius of the sphere: "))
    volume = 4 / 3 * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2
    print(f"The volume of the sphere is {volume:.2f} and the area of the sphere is {area:.2f}")

main()
