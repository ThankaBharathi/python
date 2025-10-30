a,b = 5,10
a1,b1 = a,b
while b1 != 0:
    a1,b1 = b1, a1 % b1
gcd = a1
lcm = (a * b) // gcd
print([lcm,gcd])