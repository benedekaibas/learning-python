"""
Írj egy Python programot, amely megmondja előfordul-e (igen/nem) a Debrecen szó a temp.txt
fájlban!
"""

#this file opens the temp.txt file since it is required based on the readme

filename = "temp.txt"
count = 0
with open(filename, "r") as fh:
    content = fh.read()
    lowerText = content.lower()
    print(lowerText)
    if "debrecen" in lowerText:
        count += 1
    print(count)

    




