# Q63. Hollow Hourglass Pattern
n = int(input("Size: "))

for row in range(n, 0, -1):
    for space in range(n - row):
        print(" ", end="")

    if row == n:
        for star in range(2 * n - 1):
            print("*", end="")
        print()
    elif row == 1:
        print("*")
    else:
        print("*", end="")
        for space in range(2 * row - 3):
            print(" ", end="")
        print("*")

for row in range(2, n + 1):
    for space in range(n - row):
        print(" ", end="")

    if row == n:
        for star in range(2 * n - 1):
            print("*", end="")
        print()
    else:
        print("*", end="")
        for space in range(2 * row - 3):
            print(" ", end="")
        print("*")


# Q64. Right Pascal's Triangle
n = int(input("Size: "))

for row in range(1, n + 1):
    for star in range(row):
        print("*", end="")
    print()

for row in range(n - 1, 0, -1):
    for star in range(row):
        print("*", end="")
    print()


# Q65. Pattern Size Challenge
# Run the same pattern with sizes 3, 5, and 7.
for n in (3, 5, 7):
    print("Pattern size:", n)
    for row in range(1, n + 1):
        for star in range(row):
            print("*", end="")
        print()
    print()