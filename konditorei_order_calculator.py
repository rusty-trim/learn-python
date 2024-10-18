# konditorei_order_calculator.py
#   A program that calculates the cost of an order at the Konditorei coffee shop.

def main():
    print("This is a program that calulcates the cost of an order at the Konditorei Coffee Shop based on the number of pounds you wish to order.")
    print()
    
    lbs = float(input("Enter the pounds of coffee you wish to order: "))
    shipping = 0.86 * lbs + 1.50
    cost = 10.50 * lbs + shipping

    print(f"Your order will be ${cost:.2f}")

main()
