#Bunch of exercises for practicing list in python and other things

torpok = ['Tudor', 'Vidor', 'Szende', 'Szundi', 'Hapci', 'Kuka', 'Morgó']
weasleyk = ['Bill', 'Charlie', 'Percy', 'Fred', 'George', 'Ron', 'Ginny']
#             0         1         2       3        4        5       6
zsirafok = ["Abigél", "Benő", "Zsebi"]

arlie = zsirafok.append("arlie")
gin = zsirafok.append("Gin")
print(weasleyk[2])
print([weasleyk[3]], [weasleyk[4]])
print([weasleyk[0]], [weasleyk[1]], [weasleyk[2]], [weasleyk[3]])
print(zsirafok[3])
print(zsirafok[4])

#Írjon olyan kódot, ami megmondja, hogy Ron hányadik Weasley testvér

place_ron = weasleyk.index('Ron')
print(f"Ron az {place_ron} testvér.")

#Ron ábécé sorrendben hányadik Weasley testvér?

ron_place_abc = sorted(['Bill', 'Charlie', 'Percy', 'Fred', 'George', 'Ron', 'Ginny'])
print(ron_place_abc)
index_of_ron = ron_place_abc.index('Ron')
#we have to include -1 since python counts from 0
print(index_of_ron - 1)

#Írjon olyan kódot, ami lemásolja a weasleyk listát és a másolatból kitörli Percy-t.

new_weasleyk_list = weasleyk
print(new_weasleyk_list)
new_weasleyk_list.remove('Percy')
print(new_weasleyk_list)

#Írjon programot, ami beolvas egy szöveget, és megmondja, hány e betű van benne.

text = str(input('Enter a text: '))
lower_case = text.lower()
count_e = lower_case.count("e")

print(count_e)







