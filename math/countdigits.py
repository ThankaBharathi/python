n = 2446
count = 0
temp = n
while n > 0:
    last_digit = n % 10
    if last_digit != 0 and temp % last_digit == 0:
        count += 1
    n //= 10
print(count)