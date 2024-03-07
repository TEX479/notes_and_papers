'''
USAGE:

'''

interrupt = False

def rsa_modul(text:int, key:int, modulo:int) -> int:
    return pow(text, key, modulo)

def get_input(input_type:str, validation_function=None) -> int:
    while True:
        user_input = input(f"> {input_type} = ")
        try:
            user_input = int(user_input)
        except KeyboardInterrupt:
            interrupt = True
            exit()
        except:
            user_input = -1
        
        if validation_function == None:
            break
        if validation_function(user_input):
            break
        print("invalid input!")
    return user_input

def gez(number):
    return (number >= 0)



print("Strg+C beendet das Programm\n\n\n")

try:
    while not interrupt:
        key = get_input("Schlüssel (Exponent)", gez)
        modulo = get_input("Modulo (zweiter Teil des öffentlichen Schlüssels)", gez)
        text = get_input('"Text" (Zahl zum Ver-/Entschlüsseln)', gez)

        print(f"Ergebnis (je nach Eingaben verschlüsselt oder entschlüsselt): {rsa_modul(text, key, modulo)}")
except KeyboardInterrupt:
    exit()
except Exception as e:
    print(e)
