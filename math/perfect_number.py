n = 7
sum = 1
if n <= 1:
    print(False)
i = 2
while i * i <= n:
    if n % i == 0:
        sum += i
        if i != n // i:
            sum += n // i
    i += 1
print(sum == n)
    
        