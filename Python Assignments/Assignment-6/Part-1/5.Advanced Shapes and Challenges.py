# Q43. Butterfly Pattern
n = int(input("Size: "))

for row in range(1, n + 1):
    for star in range(row):
        print("*", end="")
    for space in range(2 * (n - row)):
        print(" ", end="")
    for star in range(row):
        print("*", end="")
    print()

for row in range(n - 1, 0, -1):
    for star in range(row):
        print("*", end="")
    for space in range(2 * (n - row)):
        print(" ", end="")
    for star in range(row):
        print("*", end="")
    print()


# Q44. Hollow Hourglass
n = int(input("Size: "))

for row in range(n, 0, -1):
    for space in range(n - row):
        print(" ", end="")

    if row == n or row == 1:
        for star in range(2 * row - 1):
            print("*", end="")
        print()
    else:
        print("*", end="")
        for space in range(2 * row - 3):
            print(" ", end="")
        print("*")

for row in range(2, n + 1):
    for space in range(n - row):
        print(" ", end="")

    if row == n:
        for star in range(2 * row - 1):
            print("*", end="")
        print()
    else:
        print("*", end="")
        for space in range(2 * row - 3):
            print(" ", end="")
        print("*")


# Q45. Alphabet Diamond
n = int(input("Size: "))

for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for letter_number in range(1, row + 1):
        print(chr(64 + letter_number), end="")
    for letter_number in range(row - 1, 0, -1):
        print(chr(64 + letter_number), end="")
    print()

for row in range(n - 1, 0, -1):
    for space in range(n - row):
        print(" ", end="")
    for letter_number in range(1, row + 1):
        print(chr(64 + letter_number), end="")
    for letter_number in range(row - 1, 0, -1):
        print(chr(64 + letter_number), end="")
    print()


# Q46. Pascal's Triangle
n = int(input("Number of rows: "))

for row in range(n):
    for space in range(n - row - 1):
        print(" ", end="")

    value = 1
    for col in range(row + 1):
        print(value, end=" ")
        value = value * (row - col) // (col + 1)
    print()


# Q47. Heart Pattern
n = int(input("Size: "))

for row in range(n // 2, n, 2):
    for space in range(n // 2 - row + 1):
        print(" ", end="")
    for star in range(row + 1):
        print("*", end="")
    for space in range(n - row - 1):
        print(" ", end="")
    for space in range(n - row - 1):
        print(" ", end="")
    for star in range(row + 1):
        print("*", end="")
    print()

for row in range(n, 0, -1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(2 * row - 1):
        print("*", end="")
    print()


# Q48. Hollow Heart
n = int(input("Size: "))

print(" **   **")
print("*  * *  *")
print("*   *   *")

for row in range(1, n - 2):
    for space in range(row):
        print(" ", end="")
    print("*", end="")
    for space in range(2 * (n - row - 2) - 1):
        print(" ", end="")
    print("*")

for space in range(n - 1):
    print(" ", end="")
print("*")


# Q49. Star-and-Space Center Pattern
n = int(input("Enter an odd size: "))
middle = n // 2

for row in range(n):
    for col in range(n):
        if col == row or col == n - row - 1 or row == middle:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q50. Custom Symbol Square
n = int(input("Size: "))
symbol = input("Symbol: ")

for row in range(n):
    for col in range(n):
        print(symbol, end="")
    print()


# Q51. User-Sized Hollow Rectangle
rows = int(input("Rows: "))
columns = int(input("Columns: "))

for row in range(rows):
    for col in range(columns):
        if row == 0 or row == rows - 1 or col == 0 or col == columns - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q52. Create Your Own Pattern
n = int(input("Size: "))

for row in range(1, n + 1):
    for col in range(row):
        print("#", end="")
    print()

# Q53. Number Increasing Reverse Pyramid
n = int(input("Size: "))

for row in range(n, 0, -1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()


# Q54. Square Fill Pattern
n = int(input("Size: "))

for row in range(n):
    for col in range(n):
        print("*", end=" ")
    print()


# Q55. Left Half Pyramid
n = int(input("Size: "))

for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(2 * row - 1):
        print("*", end="")
    print()

# Q56. Reverse Right Half Pyramid
n = int(input("Size: "))

for row in range(n, 0, -1):
    for star in range(row):
        print("*", end="")
    print()


# Q57. Left Half Pyramid — Increasing
n = int(input("Size: "))

for row in range(1, n + 1):
    for star in range(row):
        print("*", end="")
    print()


# Q58. Reverse Left Half Pyramid
n = int(input("Size: "))

for row in range(n, 0, -1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(row):
        print("*", end="")
    print()


# Q59. Triangle Star Pattern
n = int(input("Size: "))

for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(row):
        print("*", end="")
    print()


# Q60. Mirror-Image Number Triangle
n = int(input("Size: "))

for row in range(1, n + 1):
    for space in range(row - 1):
        print(" ", end="")
    for number in range(row, n + 1):
        print(number, end=" ")
    print()


# Q61. Hollow Reverse Triangle
n = int(input("Size: "))

for row in range(n, 0, -1):
    spaces_before = n - row
    for space in range(spaces_before):
        print(" ", end="")

    for col in range(row):
        if row == n or row == 1 or col == 0 or col == row - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q62. Hollow Diamond Pyramid
n = int(input("Size: "))

for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")

    if row == 1:
        print("*")
    else:
        print("*", end="")
        for space in range(2 * row - 3):
            print(" ", end="")
        print("*")

for row in range(n - 1, 0, -1):
    for space in range(n - row):
        print(" ", end="")

    if row == 1:
        print("*")
    else:
        print("*", end="")
        for space in range(2 * row - 3):
            print(" ", end="")
        print("*")


