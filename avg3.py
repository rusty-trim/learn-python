# avg2.py
#   A simple program to average three exam scores
#   Illustrates use of multiple input

def main():
    print("This program computes the average of two exam scores.")

    score1, score2, score3 = eval(input("Enter three scores seperated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is:", average)

main()
