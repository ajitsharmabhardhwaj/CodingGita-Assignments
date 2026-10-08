# Q15. Factorial of a Number
n = int(input("Enter N: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print(factorial)


# Q16. Factorial from 1 to N
n = int(input("Enter N: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i
    print(i, "! =", factorial)


# Q17. Product of Even Numbers
n = int(input("Enter N: "))
product = 1

for i in range(2, n + 1):
    if i % 2 == 0:
        product = product * i

print(product)


# Q18. Product of Odd Numbers
n = int(input("Enter N: "))
product = 1

for i in range(1, n + 1):
    if i % 2 != 0:
        product = product * i

print(product)


# Q19. Double Factorial - Even Numbers
n = int(input("Enter even number: "))
product = 1

for i in range(2, n + 1):
    if i % 2 == 0:
        product = product * i

print(product)


# Q20. Sum of Squares
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total = total + i ** 2

print(total)


# Q21. Sum of Cubes
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total = total + i ** 3

print(total)


# Q22. Factorial-Based Sum
n = int(input("Enter N: "))
factorial = 1
total = 0

for i in range(1, n + 1):
    factorial = factorial * i
    total = total + factorial

print(total)
