import os


def vig(t,k):return"".join([chr((((ord(t[i])&31)+(ord(k[i%len(k)])&31)-2)%26)+65+(ord(t[i])&32))if ord(t[i])in(list(range(65,91))+list(range(97,123)))else t[i]for(i)in range(len(t))])

'''
def vig(t,k):
    return "".join([chr((((ord(t[i])&31)
                          +(ord(k[i%len(k)])&31)
                          -2)%26)
                        +65+(ord(t[i])&32))
                    if ord(t[i]) in (list(range(65,91))+list(range(97,123))) else t[i] for i in range(len(t))])
'''

def vigB(text, key):
    '''
    "vigB" oder auch "VigenèreBeautiful" ist die schöngeschriebne version des verwendeten vig().
    Die Implementierung ist wie folgt:
    Der Schlüssel wird wiederholend über den gesamten Text gelegt, und auf alle verschlüsselbaren Zeichen angewandt.
    '''
    text_encrypted = ""
    for i_text in range(len(text)):
        character = text[i_text]
        # wenn das Zeichen ein ASCII-Buchstabe ist:
        if ord(character) in (list(range(65,91)) + list(range(97,123))):
            '''
            "alphabetical": Index des Zeichens im Alphabet (a->0, b->1, c->2, ..., z->25)
            '''
            alphabetical_character = ord(character)&31 -1
            alphabetical_key = ord(key[i_text%len(key)])&31 -1
            alphabetical_encrypted = (alphabetical_character + alphabetical_key) % 26
            text_encrypted += chr(alphabetical_encrypted + ord(character)&96 +1)
        else:
            text_encrypted += character
    return text_encrypted

def validate_input(string: str, is_path:bool=True):
    # return (text: <str, None>, is_valid: bool) 
    '''if len(string) == 0:
        return (None, False)
    if not is_path:
        return (string, True)'''
    if os.path.isfile(string):
        with open(path, "r") as f:
            text = f.read()
        return (text, True)
    else:
        return (None, False)

def no_umlaute(text:str) -> str:
    text = text.replace("Ä", "Ae").replace("ä", "ae")
    text = text.replace("Ö", "Oe").replace("ö", "oe")
    text = text.replace("Ü", "Ue").replace("ü", "ue")
    text = text.replace("ẞ", "SS").replace("ß", "ss")
    return text

def print_break():
    print("--------------------")




# Eingabe des Textes
while True:
    print("1: Text manuell eingeben\n2: Text aus Datei laden (die Datei muss mit vollem Pfad angegeben werden)")
    option = input("> ")
    if option == "1":
        text = input("Text:\n")
        break
    elif option == "2":
        path = input("Datei mit Pfad:\n")
        (text, is_valid) = validate_input(path, True)
        if is_valid:
            break
        else:
            print("Fehler: Ungültige eingabe")
    else:
        print("Fehler: Ungültige eingabe")
text = no_umlaute(text)
#print("text:\n" + text)
print_break()

# Eingabe des Schlüssels
while True:
    print("1: Schlüssel manuell eingeben\n2: Schlüssel aus Datei laden (die Datei muss mit vollem Pfad angegeben werden)")
    option = input("> ")
    if option == "1":
        key = input("Schlüssel:\n")
        break
    elif option == "2":
        path = input("Datei mit Pfad:\n")
        (key, is_valid) = validate_input(path, True)
        if is_valid:
            break
        else:
            print("Fehler: Ungültige eingabe")
    else:
        print("Fehler: Ungültige eingabe")
key = no_umlaute(key)
print_break()

verschlüsselt = vig(text, key)
print(f"Verschlüsselter Text:\n{verschlüsselt}")


# Häufigkeitsverteilung
häufigkeit = {}
len_text = 0
alphabet = [chr(i) for i in range(65, 65+26)]
for i in alphabet:
    häufigkeit[i] = 0
#print(häufigkeit)
for i in verschlüsselt:
    if i.upper() in alphabet:
        häufigkeit[chr(64+(ord(i)&31))] += 1
        len_text += 1

# schönes printen der Häufigkeit
häufigkeit_str = str(häufigkeit)[1:-1].replace(", ", "\n")
print_break()
print("Häufigkeitsverteilung:")
print(häufigkeit_str)



#============== BEGINN DER WAGHALIGEN AUFGABE ==============
# Nicht gelöst, weil: Verzweiflung an der Unklarheit der Dokumentation
 
'''koinzidenzindex = 0
for i in alphabet:
    koinzidenzindex += ((häufigkeit[i]) / len_text) ** 2
print_break()
print(f"Koinizidenzindex:\t{koinzidenzindex}")


i_max = koinzidenzindex
# ^ stimmt das? in der v02_doku.pdf ist nicht eindeutig bestimmt, was "Imax" ist, falls diese formel nicht zutreffen sollte
i_min = 1/len(alphabet)

schlüssellänge = ((i_max-i_min) * len_text) / (koinzidenzindex * (len_text - 1) - i_min * len_text + i_max)

print(f"vermutete Schlüsselänge: {schlüssellänge}")'''