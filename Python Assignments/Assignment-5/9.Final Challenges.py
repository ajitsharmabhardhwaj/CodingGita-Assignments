# Q68. Number Profile
n = int(input("Enter number: "))
temp = n

digits = 0
total = 0
largest = 0
smallest = 9
even = 0
odd = 0

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10

        digits = digits + 1
        total = total + digit

        if digit > largest:
            largest = digit

        if digit < smallest:
            smallest = digit

        if digit % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1

        temp = temp // 10

print("Digits:", digits)
print("Sum:", total)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Digits:", even)
print("Odd Digits:", odd)


# Q69. String Balance Challenge
text = input("Enter string: ")

total = 0
vowels = 0
consonants = 0
uppercase = 0
lowercase = 0
even_index = 0

for i in range(len(text)):
    character = text[i]
    total = total + 1

    if i % 2 == 0:
        even_index = even_index + 1

    if character != " ":
        if character.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

        if character.isupper():
            uppercase = uppercase + 1
        elif character.islower():
            lowercase = lowercase + 1

print("Total Characters:", total)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Even Index Characters:", even_index)