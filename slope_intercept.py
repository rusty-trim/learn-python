# slope_intercept.py
#   A program that calculates the slope of a line through two (non-vertical) points

def main():
    print("This program calculates the slope of a line through two (non-vertical) points.")

    x1 = float(input("Enter the x1 coordinate: "))
    y1 = float(input("Enter the y1 coordinate: "))

    x2 = float(input("Enter the x2 coordinate: "))
    y2 = float(input("Enter the y2 coordinate: "))

    if x1 == x2:
        print("Both points cannot share the same x coordinate (this would result in a vertical line).")
        return

    slope = (y2 - y1)/(x2 - x1)

    print(f"The slope of the line is: {slope:.2f}")

main()
