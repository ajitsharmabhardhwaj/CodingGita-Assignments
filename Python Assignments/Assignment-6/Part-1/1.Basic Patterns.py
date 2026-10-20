
# Q1. Solid Square
n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()


# Q2. Solid Rectangle
rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print()


# Q3. Increasing Star Triangle
n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


# Q4. Increasing Number Triangle
n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Q5. Repeated Number Triangle
n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()


# Q6. Repeated Alphabet Triangle
n = int(input("Enter size: "))

for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end="")
    print()


# Q7. Alphabet Triangle
n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


# Q8. Continuous Number Triangle
n = int(input("Enter size: "))
number = 1

for i in range(1, n + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()


# Q9. Alternating 0-1 Triangle
n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()


# Q10. Decreasing Star Triangle
n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# Q11. Decreasing Number Triangle
n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Q12. Decreasing Alphabet Triangle
n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
