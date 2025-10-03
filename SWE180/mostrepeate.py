a = "swiss"

count = {}
for char in a:
    count[char] = count.get(char, 0)+1
for b in a:
    if count[b] == 1:
        print(b)
        break
 # repeated charector