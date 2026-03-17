string = "Thanka Bharathi T M"

count = 1 

for char in string:
    if char == " ":
        count += 1 

print(count)

# optimized

string = "Thanka Bharathi T M"
count = len(string.split())
print(count)