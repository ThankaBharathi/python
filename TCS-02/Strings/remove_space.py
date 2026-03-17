def remove_space(stringg):
    result = ""
    
    for char in stringg:
        if char != " ":
            result += char
    
    return result

stringg = "Thanka Bharathi"
print(remove_space(stringg))


# Optimized 
string = "Thanka Bharathi"

result = string.replace(" ", "")
print(result)