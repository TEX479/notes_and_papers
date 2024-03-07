'''
USAGE:
einfach ausführen und die geforderten Parameter eingeben ;)
'''


p:int = 0 # ="primzahl"
pw:int = 0 # ="primitivwurzel"
ps1:int = 0 # ="privatschlüssel 1"
num2:int = 0 # ="zahl des partners"
gs:int = 0 # ="geheimschlüssel"


def is_prime(number:int):
    if number < 2:
        return False
    if number == 2:
        return True
    for i in range(2, int(number**0.5)):
        if number % i == 0:
            return False    
    return True

def is_pw(primzahl, primitivwurzel):
    ergebnisse = []
    for i in range(1, primzahl):
        ergebnis = primitivwurzel**i % primzahl
        print(f"primitivwurzel**{i} % primzahl = {ergebnis}")
        ergebnisse.append(ergebnis)
    
    for i in range(1, primzahl):
        if not (i in ergebnisse):
            return False
    else:
        return True

def num4pardner(p:int, pw:int, ps1:int):
    return pow(pw, ps1, p)

#input für Primzahl
while True:
    p = input("> Primzahl = ")
    try:
        p = int(p)
    except:
        p = 0
    if is_prime(p):
        break
    print("invalid input!")

#input für Primitivwurzel
while True:
    pw = input("> Primitivwurzel = ")
    try:
        pw = int(pw)
    except:
        pw = 0
    if is_pw(p):
        break
    print("invalid input!")

#input für Privatschlüssel
while True:
    ps1 = input("> privater Schlüssel = ")
    try:
        ps1 = int(pw)
    except:
        ps1 = 0
    if (ps1 in range(1, p)):
        break
    print("invalid input!")

print(f"Zahl für den Partner: {num4pardner(p, pw, ps1)}")

#input für weiterführender Schlüssel des Partners
while True:
    num2 = input("> Zahl des Partners = ")
    try:
        num2 = int(pw)
    except:
        num2 = 0
    if (num2 in range(1, p)):
        break
    print("invalid input!")

gs = num4pardner(p, pw, num2)
print(f"Geheimschlüssel: {gs}")
