# Q11. Decreasing Number Triangle
n = int(input("Size: "))
for row in range(n, 0, -1):
    for number in range(1, row + 1):
        print(number, end="")
    print()


# Q12. Decreasing Alphabet Triangle
n = int(input("Size: "))
for row in range(n, 0, -1):
    for letter_number in range(1, row + 1):
        print(chr(64 + letter_number), end="")
    print()


# Q13. Right-Aligned Half Pyramid
n = int(input("Size: "))
for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(row):
        print("*", end="")
    print()


# Q14. Inverted Right-Aligned Half Pyramid
n = int(input("Size: "))
for row in range(n, 0, -1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(row):
        print("*", end="")
    print()


# Q15. Star Pyramid
n = int(input("Size: "))
for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(2 * row - 1):
        print("*", end="")
    print()


# Q16. Inverted Star Pyramid
n = int(input("Size: "))
for row in range(n, 0, -1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(2 * row - 1):
        print("*", end="")
    print()


# Q17. Solid Diamond
n = int(input("Size: "))
for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(2 * row - 1):
        print("*", end="")
    print()

for row in range(n - 1, 0, -1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(2 * row - 1):
        print("*", end="")
    print()


# Q18. Rhombus
n = int(input("Size: "))
for row in range(n):
    for space in range(n - row - 1):
        print(" ", end="")
    for star in range(n):
        print("*", end="")
    print()


# Q19. Mirrored Number Pattern
n = int(input("Size: "))
for row in range(1, n + 1):
    for number in range(1, row + 1):
        print(number, end="")
    for space in range(2 * (n - row)):
        print(" ", end="")
    for number in range(row, 0, -1):
        print(number, end="")
    print()


# Q20. Centered Number Pyramid
n = int(input("Size: "))
for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for number in range(1, row + 1):
        print(number, end=" ")
    print()


# Q21. Palindromic Number Pyramid
n = int(input("Size: "))
for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for number in range(1, row + 1):
        print(number, end="")
    for number in range(row - 1, 0, -1):
        print(number, end="")
    print()


# Q22. Alphabet Palindrome Pyramid
n = int(input("Size: "))
for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for letter_number in range(1, row + 1):
        print(chr(64 + letter_number), end="")
    for letter_number in range(row - 1, 0, -1):
        print(chr(64 + letter_number), end="")
    print()


# Q23. Reverse-Starting Alphabet Triangle
n = int(input("Size: "))
for row in range(1, n + 1):
    start = n - row + 1
    for letter_number in range(start, n + 1):
        print(chr(64 + letter_number), end=" ")
    print()
