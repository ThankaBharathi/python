string = "Thanka Bharathi"
vowels = "aeiouAEIOU"
result = ""

for char in string:
    if char not in vowels:
        result += char

print(result)

#optimized 
string = "Thanka Bharathi"

result = "".join([c for c in string if c.lower() not in "aeiou"])
print(result)