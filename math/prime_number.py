n = 7
for i in range(1,int(n ** 0.5)+1):
    if n % i == 0:
        print(False)
print(False if n == 1 else True)

