# FInd a frequency of a charector in an string 

arr = [0] * 26
s = input("Enter a string: ").upper()

for ch in s:
    if 'A' <= ch <= 'Z':
        index = ord(ch) - ord('A')
        arr[index] += 1 

for i in range(26):
    ch = chr(i + ord('A'))
    print(f"{ch}:{arr[i]}", end = "->")

