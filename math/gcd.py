a,b = 20,28
while b != 0:
    a,b = b, a % b
print(a)