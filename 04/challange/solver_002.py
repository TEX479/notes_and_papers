filename = "Text09.txt"
with open("/home/tex/Schule/info/04/challange/" + filename, "rb") as f:
    contents = f.read().decode()
contents = contents.split(" ")
contents = "".join([chr(int(i, 16)) for i in contents])

print(len(contents))
