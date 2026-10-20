# Q86. Count Words
text = input("Sentence: ")
word_count = len(text.split())
print(word_count)


# Q87. Replace All 'a' with 'e'
text = input("String: ")
result = ""

for character in text:
    if character == "a":
        result += "e"
    else:
        result += character

print(result)


# Q88. Check for a Character
text = input("String: ")
character_to_find = input("Character: ")
found = False

for character in text:
    if character == character_to_find:
        found = True

print(found)


# Q89. Compare Two Strings
first = input("First string: ")
second = input("Second string: ")

print(first == second)


# Q90. Count Digits in a String
text = input("String: ")
digit_count = 0

for character in text:
    if "0" <= character <= "9":
        digit_count += 1

print(digit_count)


# Q91. Count Uppercase Letters
text = input("String: ")
uppercase_count = 0

for character in text:
    if "A" <= character <= "Z":
        uppercase_count += 1

print(uppercase_count)


# Q92. Count Lowercase Letters
text = input("String: ")
lowercase_count = 0

for character in text:
    if "a" <= character <= "z":
        lowercase_count += 1

print(lowercase_count)


# Q93. Remove All Vowels
text = input("String: ")
result = ""

for character in text:
    if character not in "aeiouAEIOU":
        result += character

print(result)


# Q94. Remove All Digits
text = input("String: ")
result = ""

for character in text:
    if not ("0" <= character <= "9"):
        result += character

print(result)


# Q95. Toggle Character Case
text = input("String: ")
result = ""

for character in text:
    if "a" <= character <= "z":
        result += chr(ord(character) - 32)
    elif "A" <= character <= "Z":
        result += chr(ord(character) + 32)
    else:
        result += character

print(result)

