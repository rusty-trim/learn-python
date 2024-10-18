# lightning_strike_and_mile_distance.py
#   A program that determines the distance to a lightning strike based on the time elapsed between the flash and the sound of thunder.

def main():
    time_elapsed = float(input("Enter the seconds that elasped between the flash and the sound of thunder: "))
    distance_feet = 1100 * time_elapsed
    distance_miles = distance_feet / 5280
    
    print(f"The distance to a lightning strike was {distance_miles:.2f} miles.")

main()
