import tkinter as tk

def int2anybase(number:int, base:int):
    number_ = []
    while number > 0:
        number_.append(number%base)
        number = number//base
    number_.reverse()
    return number_

def transmute(way: str, list2transform:list, rotation):
    transformed_list = [0,0,0,0,0,0]
    if way == 1 or way == "1" or way == "wog-oby":
        transformed_list[0] = list2transform[5]
        transformed_list[1] = list2transform[4]
        transformed_list[2] = list2transform[0]
        transformed_list[3] = list2transform[3]
        transformed_list[4] = list2transform[2]
        transformed_list[5] = list2transform[1]
    elif way == 2 or way == "2" or way == "oby-wrb":
        transformed_list[0] = list2transform[2]
        transformed_list[1] = list2transform[3]
        transformed_list[2] = list2transform[1]
        transformed_list[3] = list2transform[5]
        transformed_list[4] = list2transform[4]
        transformed_list[5] = list2transform[0]
    elif way == 3 or way == "3" or way == "120" or way == "120°":
        transformed_list[0] = list2transform[1]
        transformed_list[1] = list2transform[2]
        transformed_list[2] = list2transform[0]
        transformed_list[3] = list2transform[4]
        transformed_list[4] = list2transform[5]
        transformed_list[5] = list2transform[3]
        rotation[0] = (rotation[0] + 120) % 360
    elif way == 4 or way == "4" or way == "240" or way == "240°":
        transformed_list[0] = list2transform[2]
        transformed_list[1] = list2transform[0]
        transformed_list[2] = list2transform[1]
        transformed_list[3] = list2transform[5]
        transformed_list[4] = list2transform[3]
        transformed_list[5] = list2transform[4]
        rotation[0] = (rotation[0] + 240) % 360
    else:
        raise ValueError("Input cannot be handeled")
    
    return transformed_list

def bruteforce(starting_position:list, max_moves=10, ending_position=[1,2,3,4,5,6]) -> str:
    outcomes = []
    #start = time.time()
    for i in range(4**max_moves):
        #print(f"\r\t{i/(4**max_moves)*100:.2}%", end=" ")
        middles = starting_position.copy()
        rotation = [0]
        moves = int2anybase(i, 4)
        moves = [str(i2+1) for i2 in moves]
        for move in moves:
            middles = transmute(move, middles, rotation)
        if middles == ending_position and rotation[0] == 0:
            outcomes.append([moves, middles])
            break
    else:
        outcomes = [[f"found no solution in within {max_moves} moves"]]
    
    return ''.join(outcomes[0][0])


middles = []
colors = ["white", "orange", "green", "red", "blue", "yellow"]
colors_short = [i[0] for i in colors]

def parse_input(string:str) -> (bool, list):
    output_list = [0] *6
    if len(string) != 6:
        return (False, "input length did not match 6")
    for color in colors_short:
        if not color in string:
            return (False, f"did not include letter {color}")
    for color_index in range(len(string)):
        output_list[color_index] = colors_short.index(string[color_index]) +1 #+1, cuz the list has to be from 1 to 6
    return (True, output_list)

while True:
    print(f"Input the 6-letter- combination of where the colors are on your skewb, so that the following rules apply:")
    print(f"(1) The there is one letter for each color ({str(colors_short)} for {str(colors)})")
    print(f"(2) The order of the input colors corresponds to the order, you find the middle pieces, if you look at the outer pieces colors in the following order:\n    {str(colors)}")
    input_string = input("> ")
    (valid_input, middles) = parse_input(input_string)

    if valid_input:
        break
    else:
        print(f"invalid input: {middles}")

solution = bruteforce(middles)
print(f"solution-string: '{solution}'")
print(f"see the docs in crazy_skewb.md for a guide on how to use the output")
