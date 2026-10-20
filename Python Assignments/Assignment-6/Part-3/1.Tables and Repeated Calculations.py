# Q96. Multiplication Tables from 1 to N
n = int(input("N: "))
k = int(input("K: "))

for number in range(1, n + 1):
    for multiplier in range(1, k + 1):
        print(f"{number} x {multiplier} = {number * multiplier}")


# Q97. Number and Its Divisors
n = int(input("N: "))

for number in range(1, n + 1):
    print(f"{number}:", end="")
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            print(f" {divisor}", end="")
    print()


# Q98. Count Divisors for Every Number
n = int(input("N: "))

for number in range(1, n + 1):
    divisor_count = 0

    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisor_count += 1

    print(f"{number}: {divisor_count}")


# Q99. Perfect Numbers in a Range
n = int(input("N: "))

for number in range(2, n + 1):
    divisor_sum = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor

    if divisor_sum == number:
        print(number)


# Q100. Prime Numbers in a Range — Count Each Check
n = int(input("N: "))

for number in range(2, n + 1):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")




