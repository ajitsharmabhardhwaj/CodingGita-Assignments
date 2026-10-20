# Q33. Hollow Square
n = int(input("Size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q34. Hollow Rectangle
rows = int(input("Rows: "))
columns = int(input("Columns: "))

for row in range(rows):
    for col in range(columns):
        if row == 0 or row == rows - 1 or col == 0 or col == columns - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q35. Hollow Number Square
n = int(input("Size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1:
            print("1", end="")
        else:
            print("0", end="")
    print()


# Q36. Hollow Right-Angled Triangle
n = int(input("Size: "))

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if row == 1 or row == n or col == 1 or col == row:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q37. Hollow Inverted Triangle
n = int(input("Size: "))

for row in range(n, 0, -1):
    for col in range(1, row + 1):
        if row == n or row == 1 or col == 1 or col == row:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q38. Hollow Pyramid
n = int(input("Size: "))

for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")

    if row == 1:
        print("*")
    elif row == n:
        for star in range(2 * n - 1):
            print("*", end="")
        print()
    else:
        print("*", end="")
        for space in range(2 * row - 3):
            print(" ", end="")
        print("*")


# Q39. Hollow Diamond
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


# Q40. X Pattern
n = int(input("Size (use an odd number): "))

for row in range(n):
    for col in range(n):
        if col == row or col == n - row - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q41. Cross Pattern
n = int(input("Size (use an odd number): "))
middle = n // 2

for row in range(n):
    for col in range(n):
        if row == middle or col == row or col == n - row - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q42. Star Cross with Four Arms
n = int(input("Enter an odd size: "))

for row in range(n):
    for col in range(n):
        if col == row or col == n - row - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
