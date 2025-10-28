n = int(input("Enter a input: "))
fact = []
for i in range(1, int(n ** 0.5)+1):
    if n % i == 0:
        fact.append(i)
        if i * i != n:
            fact.append(n//i)
print(sorted(fact))

    