# average_of_series_of_numbers.oy
#   A program that finds the average of a series of numbers entered by the user.

def main():
    print("This is a progam to find the average of a series of numbers entered by the user.")
    print()
    
    n = int(input("Enter the amount of numbers you want to add: "))

    if n <= 0:
        print("Error: You entered an incorrect amount of numbers to be added.")
        return

    result = 0

    for i in range(1, n + 1):
        result += float(input(f"Enter number {i}: "))

    result = result / n

    print(f"The average of the series of numbers is {result:.2f}")

main()
