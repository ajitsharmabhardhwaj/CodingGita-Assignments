# Q37. Print Characters with Index
text = input("Enter string: ")

index = 0
for character in text:
    print(index, character)
    index = index + 1


# Q38. Count Characters Without len()
text = input("Enter string: ")
count = 0

for character in text:
    count = count + 1

print(count)


# Q39. Count Vowels and Consonants
text = input("Enter string: ")
vowels = 0
consonants = 0

for character in text:
    if character != " ":
        if character.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Vowels =", vowels)
print("Consonants =", consonants)


# Q40. Character Frequency
text = input("Enter string: ")
target = input("Enter target character: ")
count = 0

for character in text:
    if character == target:
        count = count + 1

print(count)


# Q41. First Occurrence Position
text = input("Enter string: ")
target = input("Enter target character: ")
position = -1
index = 0

for character in text:
    if character == target and position == -1:
        position = index
    index = index + 1

if position == -1:
    print("Not Found")
else:
    print(position)


# Q42. Count Uppercase and Lowercase
text = input("Enter string: ")
uppercase = 0
lowercase = 0

for character in text:
    if character.isupper():
        uppercase = uppercase + 1
    elif character.islower():
        lowercase = lowercase + 1

print("Uppercase =", uppercase)
print("Lowercase =", lowercase)


# Q43. Character Code Analyzer
text = input("Enter string: ")

for character in text:
    print(character, ord(character))


# Q44. String Without Vowels
text = input("Enter string: ")
result = ""

for character in text:
    if character.lower() not in "aeiou":
        result = result + character

print(result)

