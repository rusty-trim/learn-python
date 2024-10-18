# sum_user_input.py
#   A program to sum a series of numbers entered by a user.

def main():
    print("This is a program to sum a series of numbers entered by the user.")
    print()
    
    n = int(input("Enter the amount of numbers you will want to add: "))

    if n < 0:
        print("Error: You entered an incorrect amount of numbers to be added.")
        return

    result = 0
    
    for i in range(1, n + 1):
        result += float(input(f"Enter Number {i}: "))

    print(f"The sum of the numbers is {result:.2f}")

main()
