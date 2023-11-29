#path to the code: 
#C:\Users\kaiba\OneDrive\Asztali gép\learning\string_finder.py

word = "kjhfdssjdnbsdbdfkbjkldbjdfbdbbbbdfklgfldjkgljkdfjklbjkldbfdkljgkjlfdjklgdfjklbkdfjklbjkffbbjkkjlfbz"

search = ""
letter_looking_for = str(input("Enter a letter you are looking for: "))
count = 0 
#count the given letters in the string
for search in word:
    if search == letter_looking_for:
        count += 1


print(count)
        
