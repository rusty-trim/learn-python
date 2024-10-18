# fahrenheit_to_celsius.py
#   A program that converts fahrenheit to celsius
#   By: Rusty Trim

def main():
    fahrenheit = eval(input("What is the temperature in fahrenheit: "))
    celsius = 5/9 * (fahrenheit - 32)
    print(f"The temperature is {celsius} degrees celsius")

main()
