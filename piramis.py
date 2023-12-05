#Ez a program két piramist ad vissza, amelyek egy fél paralelogramma.
global ROWS
global LINES
ROWS = 10

def piramis():
    for i in range(ROWS):
        for j in range(i + 1):
            print("*", end = "")
        print("\n")
    for i in range(ROWS):
        for j in range(ROWS - i ):
            print("*", end = "")
        print("\n")
    



if __name__ == "__main__":
    piramis()














