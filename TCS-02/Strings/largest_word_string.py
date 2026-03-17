string = "Thanka Bharathi T M"

words = string.split()
largest = ""

for word in words:
    if len(word) > len(largest):
        largest = word

print(largest)

# optimized
string = "Thanka Bharathi T M"
largest = max(string.split(), key = len)
print(largest)