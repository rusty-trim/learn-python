# sum_of_first_natural_numbers.py
#   A program to find the sum of the first natural numbers provided by the input

def main():
    print("This is a program to find the sum of the first natural numbers provided by the input")
    print()
    
    n = int(input("Enter the value for n: "))

    if n < 1:
        print("Enter a positive integer for n")
        return
    
    result = 0
    
    for i in range(1, n + 1):
        result += i

    print(f"The sum of the first natural numbers is {result}")

main()
