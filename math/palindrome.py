n = 123
temp = n
reverse = 0
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10
print(reverse == n)