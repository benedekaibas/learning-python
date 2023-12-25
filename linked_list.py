"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
"""


def main():
    list_one = list(input('Enter three numbers: '))
    list_two = list(input('Etner three numbers: '))
    print(f"{list_one}\n{list_two}")

    number = 0 

    for number in list_one:
        number_one  = int(''.join(map(str, list_one)))
        number_two = int(''.join(map(str, list_two)))
        print(f"{number_one}\n{number_two}")
        break
        
    add = number_one[0] + number_two[0]
    print(add)
if __name__ == "__main__":
    main()
