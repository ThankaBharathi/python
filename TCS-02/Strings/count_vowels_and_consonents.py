string = "Thanka Bharathi"
vowels = "aeiouAEIOU"
count_vowels = 0
count_consonents = 0

for char in string:
    if char.isalpha():
        if char in vowels:
            count_vowels += 1 
        else:
            count_consonents += 1 

print(count_consonents, count_vowels)

# optimized 

string = "Thanka Bharathi"
vowels = "aeiouAEIOU"

vowels_count = sum(1 for c in string if c in vowels)
consonents_count = sum(1 for c in string if c.isalpha() and c not in vowels)

print(vowels_count)
print(consonents_count)