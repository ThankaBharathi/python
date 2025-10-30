n = 24

temp = n
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print(n ** rev)

# problem statement is reverse a number and them do a square for the orginal number