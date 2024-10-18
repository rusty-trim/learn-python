# calculator.py
#  A program that takes in input as an expression and calculates it.
#  By: Rusty Trim

def main():
  for i in range(100):
    # I know eval is not safe but I am unsure how to achieve expressional input in a good way as of now.
    exp = eval(input("Type a mathematical expression here: "))
    print(f"The answer is {exp}")

main()
