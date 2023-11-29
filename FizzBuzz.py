"""
Fizzbuzz: Koncentrációs játék, ahol 1-től kezdve soroljuk a számokat, és minden 3-mal osztahtó szám helyett azt kell mondani, 
hogy Fizz, az 5-tel oszthatók helyett, hogy Buzz. Ha 3-mal és 5-tel is osztható a szám, akkor azt kell mondani, hogy FizzBuzz.
"""

def fizzbuzz():
    start = 0 
    end = 101
    i = 1
    for i in range(start, end):
        i + 1
        print(i)
        while i % 3 == 0:
            print(f" {i}: fizz")
            break

    
if __name__ == "__main__":
    fizzbuzz()










