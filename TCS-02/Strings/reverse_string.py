def reversee(stringg):
    reverse_string = ""
    
    for i in range(len(stringg) -1,-1,-1):
        reverse_string += stringg[i]
    
    return reverse_string

stringg = "Thanka Bharathi"
print(reversee(stringg))