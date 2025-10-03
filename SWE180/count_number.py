n = 12345

count = 0
original = n
while n > 0:
    ans = n % 10
    if ans != 0 and original % ans == 0:
        count += 1
    n //= 10
print(count)

# count a number 