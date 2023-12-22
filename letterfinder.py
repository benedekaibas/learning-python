"""
Írjon programot, ami beolvas egy szöveget, majd egy betűt, és megmondja, a betű hányszor szerepel a szövegben.

"""

def letter_finder():
    text = str(input('Enter a text: '))
    letter = str(input('Enter a letter: '))

    if letter in text:
        to_lower = text.lower()
        count = to_lower.count(letter)
        print(f"We have found {count} {letter} letters in your text!")


if __name__ == "__main__":
    letter_finder()

