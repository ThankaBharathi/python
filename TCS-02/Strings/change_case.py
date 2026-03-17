string = "Thanka Bharathi T M"
result = ""

for char in string:
    if char.islower():
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
        result += char

print(result)
        
        
# optimized

string = "Thanka Bharathi T M"
result = string.swapcase()
print(result)