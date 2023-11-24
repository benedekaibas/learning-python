#path to the code: 
#C:\Users\kaiba\OneDrive\Asztali gép\learning\string_finder.py

word = "kjhfdssjdnbsdbdfkbjkldbjdfbdbbbbdfklgfldjkgljkdfjklbjkldbfdkljgkjlfdjklgdfjklbkdfjklbjkffbbjkkjlfb"

search = ""
letter_looking_for = "b"
count = 0 

for search in word:
    if search == letter_looking_for:
        count += 1 
        print(count)
        #print(count.index()) #check how should this work!
    #else:
        #print("Code not working well!")


