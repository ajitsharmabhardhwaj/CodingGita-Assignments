# Q25. Number Hourglass
n = int(input("Size: "))
for row in range(n, 0, -1):
    for number in range(1, row + 1):
        print(number, end="")
    print()

for row in range(2, n + 1):
    for number in range(1, row + 1):
        print(number, end="")
    print()


# Q26. Alphabet Hourglass
n = int(input("Size: "))
for row in range(n, 0, -1):
    for letter_number in range(1, row + 1):
        print(chr(64 + letter_number), end="")
    print()

for row in range(2, n + 1):
    for letter_number in range(1, row + 1):
        print(chr(64 + letter_number), end="")
    print()


# Q27. Alternating Star and Hash Grid
n = int(input("Size: "))
for row in range(n):
    for col in range(n):
        if (row + col) % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()


# Q28. Binary Checkerboard
n = int(input("Size: "))
for row in range(n):
    for col in range(n):
        print(1 - ((row + col) % 2), end="")
    print()


# Q29. Multiplication Grid
n = int(input("Size: "))
for row in range(1, n + 1):
    for col in range(1, n + 1):
        print(row * col, end=" ")
    print()


# Q30. Alternating-Direction Rows
n = int(input("Size: "))
for row in range(1, n + 1):
    if row % 2 == 1:
        for number in range(1, row + 1):
            print(number, end="")
    else:
        for number in range(row, 0, -1):
            print(number, end="")
    print()

# Q31. Number Diamond
n = int(input("Size: "))

for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for number in range(1, row + 1):
        print(number, end="")
    for number in range(row - 1, 0, -1):
        print(number, end="")
    print()

for row in range(n - 1, 0, -1):
    for space in range(n - row):
        print(" ", end="")
    for number in range(1, row + 1):
        print(number, end="")
    for number in range(row - 1, 0, -1):
        print(number, end="")
    print()


# Q32. Concentric Number Square
n = int(input("Size: "))
width = 2 * n - 1

for row in range(width):
    for col in range(width):
        distance_top = row
        distance_left = col
        distance_bottom = width - 1 - row
        distance_right = width - 1 - col

        nearest_edge = min(
            distance_top,
            distance_left,
            distance_bottom,
            distance_right
        )
        print(n - nearest_edge, end=" ")
    print()