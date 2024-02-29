input_string = "COOL"
e = 79 #optional mit d
N = 3961


output_string = "#".join(str(pow(ord(character), e, N)) for character in input_string)
print("verschlüsselter Text:\n" + output_string)