# triangle_area.py
#   A program that calculates the area of a triangle based on the length of its three sides.

import math

def main():
    print("This is a program that calculates the area of a triangle based on the length of its three sides.")
    print()

    a = float(input("Enter the length of side A: "))
    b = float(input("Enter the length of side B: "))
    c = float(input("Enter the length of side C: "))

    s = (a + b + c) / 2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print(f"The area of the triangle is {A:.2f}")

main()
