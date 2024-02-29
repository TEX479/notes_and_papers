e = 79
T = 3712
n = 1
while True:
    if (e*n) % T == 1:
        break
    n += 1

print(n)