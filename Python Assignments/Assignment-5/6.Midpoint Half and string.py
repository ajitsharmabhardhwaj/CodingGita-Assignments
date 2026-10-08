# Q45. Find the Middle Character
text = input("Enter string: ")
length = 0

for character in text:
    length = length + 1

middle = length // 2
print(text[middle])


# Q46. First Half and Second Half
text = input("Enter string: ")
length = 0

for character in text:
    length = length + 1

middle = length // 2

print("First Half:", text[:middle])
print("Second Half:", text[middle:])


# Q47. Split a String by Length - Odd vs Even
text = input("Enter string: ")
length = 0

for character in text:
    length = length + 1

first_half = ""
second_half = ""
middle = ""

for i in range(length):
    if length % 2 != 0:
        if i < length // 2:
            first_half = first_half + text[i]
        elif i == length // 2:
            middle = text[i]
        else:
            second_half = second_half + text[i]
    else:
        if i < length // 2:
            first_half = first_half + text[i]
        else:
            second_half = second_half + text[i]

if length % 2 != 0:
    print("First Half:", first_half)
    print("Middle:", middle)
    print("Second Half:", second_half)
else:
    print("First Half:", first_half)
    print("Second Half:", second_half)


# Q48. Compare Two Halves
text = input("Enter string: ")
length = 0

for character in text:
    length = length + 1

half = length // 2
equal = True

for i in range(half):
    if text[i] != text[i + half]:
        equal = False

if equal:
    print("Equal Halves")
else:
    print("Different Halves")


# Q49. Mirror the String
text = input("Enter string: ")
length = 0

for character in text:
    length = length + 1

symmetric = True

for i in range(length // 2):
    if text[i] != text[length - 1 - i]:
        symmetric = False

if symmetric:
    print("Symmetric")
else:
    print("Not Symmetric")


# Q50. Alternate Character Extraction
text = input("Enter string: ")
result = ""

for i in range(0, len(text), 2):
    result = result + text[i]

print(result)


# Q51. Count Characters at Even and Odd Indexes
text = input("Enter string: ")
even = 0
odd = 0

for i in range(len(text)):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even Index =", even)
print("Odd Index =", odd)


# Q52. Swap Adjacent Characters
text = input("Enter string: ")
result = ""

for i in range(0, len(text), 2):
    result = result + text[i + 1] + text[i]

print(result)
