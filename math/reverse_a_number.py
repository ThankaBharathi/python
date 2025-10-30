a = 122
ans =0
while a > 0:
    digit = a % 10
    ans = ans * 10 + digit
    a //= 10
print(ans)