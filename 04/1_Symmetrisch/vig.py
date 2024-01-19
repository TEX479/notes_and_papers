def vig(t,k):
    return"".join([chr((((ord(t[i])&31)+(ord(k[i%len(k)])&31)-2)%26)+65+(ord(t[i])&32))if ord(t[i])in(list(range(65,91))+list(range(97,123)))else t[i]for(i)in range(len(t))])
