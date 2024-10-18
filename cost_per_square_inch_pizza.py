# cost_per_square_inch_pizza.py
#   A program that calculates the cost per square inch of a circular pizza.

import math

def main():
    diameter = float(input("What is the diameter of the circular pizza (in inches): "))
    price = float(input("How much does the pizza cost (in dollars): "))
    radius = diameter / 2
    area = math.pi * radius ** 2
    cost_per_square_inch = price / area

    print(f"The cost per square inch of the pizza is ${cost_per_square_inch:.2f}")

main()
