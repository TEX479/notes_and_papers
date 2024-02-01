
def check(primzahl, primitivwurzel):
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



primzahl = 11
primitivwurzel = 6

print(check(primzahl, primitivwurzel))