# sec_to_min.py
#   A program that converts seconds to minutes
#   By: Rusty Trim

def main():
    print("This program converts seconds to minutes")
    secs = float(input("Type in the number of seconds: "))
    mins = secs / 60
    print(f"There are {secs} seconds in {mins:.2f} minutes.")

main()
