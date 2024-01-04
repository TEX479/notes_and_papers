alphabet_lower = list("abcdefghijklmnopqrstuvwxyz")
alphabet_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def vig(geheimtext, key):
    klartext = ""
    key_index = -1
    for i in geheimtext:
        i:str
        if not ((i in alphabet_lower) or (i in alphabet_upper)):
            klartext += i
            continue

        key_index = (key_index + 1) % len(key)
        if i in alphabet_lower:
            letter = alphabet_lower.index(i)
            letter = (letter - alphabet_upper.index(key[key_index].upper())) % 26
            klartext += alphabet_lower[letter]
        else:
            letter = alphabet_upper.index(i)
            letter = (letter - alphabet_upper.index(key[key_index].upper())) % 26
            klartext += alphabet_upper[letter]
    
    return klartext
        



filename = "Text08.txt"
key = "LYRICS"
with open("I:\\Kilian_Ludwig\\11\info\python\\04\challange\\" + filename, "rb") as f:
    contents = f.read().decode()
#contents = contents.split(" ")
#contents = "".join([chr(int(i, 16)) for i in contents])

contents = vig(contents, key)
print(contents)
with open("I:\\Kilian_Ludwig\\11\info\python\\04\challange\\loesungen\\" + filename, "w") as f:
    f.write(contents)