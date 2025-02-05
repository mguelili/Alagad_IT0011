text = input("Enter a string: ")


vowels = 0
consonants = 0
spaces = 0
others = 0

vowel_list_lower = ['a', 'e', 'i', 'o', 'u']
vowel_list_upper = ['A', 'E', 'I', 'O', 'U']

for char in text:
    
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        if char in vowel_list_lower or char in vowel_list_upper:
            vowels += 1
        else:
            consonants += 1
    
    elif char == ' ':
        spaces += 1
    
    else:
        others += 1


print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)
print("Other characters:", others)
