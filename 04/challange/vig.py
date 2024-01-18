def vig(text:str, key:str):
    #key = "abc"
    #text = "aaabbbccc"
    encoded = "".join([chr((((ord(text[i])&31)+(ord(key[i%len(key)])&31)-1)%26)+64+(ord(text[i])&32))if ord(text[i]) in (list(range(65,91)) + list(range(97,123))) else text[i] for i in range(len(text))])
    return encoded
