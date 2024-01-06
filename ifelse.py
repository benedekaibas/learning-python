"""
Task
Given an integer, n, perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 , print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
"""


def main():
    num = float(input("enter a number: "))
    
    if num % 2 != 0:
        print(f"{num} is an odd number!, Weird")
    elif num % 2 == 0 and 2 <= num <= 5:
        print(f"{num} is an even number and it is between 2 and 5!, Not Weird")
    elif num % 2 == 0 and 6 <= num <= 20:
        print(f"{num} is an even number and it is between 6 and 20!, Weird")
    elif num % 2 == 0 and num >= 20:
        print(f"{num} is an even number and greater than 20!, Not Weird")





if __name__ == "__main__":
    main()