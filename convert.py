# convert.py
#   A Program to convert Celsius temps to Fahrenheit
#   By: Rusty Trim

def main():

    print(f"{'Celsius':^10} | {'Fahrenheit':^12}");
    print("-" * 25)
    
    for i in range(11):
        celsius = i * 10
        fahrenheit = 9/5 * celsius + 32
        print(f"{celsius:^10} | {fahrenheit:^12}")

main()
