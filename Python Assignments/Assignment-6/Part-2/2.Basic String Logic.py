# Q76. Length of a String
text = input("String: ")
print(len(text))


# Q77. Print Each Character
text = input("String: ")

for character in text:
    print(character)


# Q78. Count Vowels
text = input("String: ")
vowel_count = 0

for character in text:
    if character in "aeiouAEIOU":
        vowel_count += 1

print(vowel_count)


# Q79. Count Consonants
text = input("String: ")
consonant_count = 0

for character in text:
    if character.isalpha() and character not in "aeiouAEIOU":
        consonant_count += 1

print(consonant_count)


# Q80. Convert to Uppercase
text = input("String: ")
print(text.upper())


# Q81. Convert to Lowercase
text = input("String: ")
print(text.lower())


# Q82. Reverse a String
text = input("String: ")
reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

print(reversed_text)


# Q83. Palindrome String
text = input("String: ")
reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

print(text == reversed_text)


# Q84. Count a Specific Character
text = input("String: ")
count = 0

for character in text:
    if character == "a" or character == "A":
        count += 1

print(count)


# Q85. Remove All Spaces
text = input("String: ")
result = ""

for character in text:
    if character != " ":
        result += character

print(result)

  
