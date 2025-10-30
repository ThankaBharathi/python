divi = 10
lis = []
for i in range(1, int(divi ** 0.5)+1):
    if divi % i == 0:
        lis.append(i)
        if i != divi // i:
            lis.append(divi // i)
print(sorted(lis))