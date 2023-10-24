letters = ['a','b','d','e','i','j','o']

def filter_vowels(letter):
    vowels = ["a","e","i","o","u"]

    if (letter in vowels):
        return True
    else:
        return False
        
filtered_vowels = filter(filter_vowels, letters)
# print(filtered_vowels)

print("The filtered vowlels are: ")

for vowel in filtered_vowels:
    print(vowel)