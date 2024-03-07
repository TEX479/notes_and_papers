def square_and_multiply(base:int, exponent:int):
    binary_length = len(f"{exponent:b}")
    result = 1
    for iteration in range(1,binary_length):
        bit = int((2**(binary_length-iteration-1) & exponent) != 0)
        
        if bit:
            result = (result**2 * base)
        else:
            result = result**2
    return result

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
    return number >= 0

if __name__ == "__main__":
    base = get_input("base", gez)
    exponent = get_input("exponent", gez)
    solution = square_and_multiply(base, exponent)
    print(f"{base}**{exponent}: {solution}")