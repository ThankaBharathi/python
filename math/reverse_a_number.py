a = 122
ans =0
while a > 0:
    ans = ans * 10 + a % 10
    a //= 10
print(ans)