# Q66. Count Digits
n = abs(int(input("Number: ")))

if n == 0:
    digits = 1
else:
    digits = 0
    while n > 0:
        digits += 1
        n //= 10

print(digits)


# Q67. Sum of Digits
n = abs(int(input("Number: ")))
digit_sum = 0

while n > 0:
    digit_sum += n % 10
    n //= 10

print(digit_sum)


# Q68. Product of Digits
n = abs(int(input("Number: ")))

if n == 0:
    product = 0
else:
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10

print(product)


# Q69. Reverse a Number
n = int(input("Number: "))
sign = -1 if n < 0 else 1
n = abs(n)
reversed_number = 0

while n > 0:
    reversed_number = reversed_number * 10 + n % 10
    n //= 10

print(sign * reversed_number)


# Q70. Palindrome Number
n = int(input("Number: "))
original = abs(n)
working_number = original
reversed_number = 0

while working_number > 0:
    reversed_number = reversed_number * 10 + working_number % 10
    working_number //= 10

print(original == reversed_number)


# Q71. Prime Number
n = int(input("Number: "))
is_prime = n >= 2
divisor = 2

while divisor * divisor <= n:
    if n % divisor == 0:
        is_prime = False
        break
    divisor += 1

print(is_prime)


# Q72. Primes from 1 to N
n = int(input("N: "))

for number in range(2, n + 1):
    is_prime = True
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(number, end=" ")


# Q73. First N Fibonacci Numbers
n = int(input("N: "))
first = 0
second = 1

for i in range(n):
    print(first, end=" ")
    first, second = second, first + second


# Q74. GCD of Two Numbers
a = int(input("First positive integer: "))
b = int(input("Second positive integer: "))

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print(a)


# Q75. LCM of Two Numbers
a = int(input("First positive integer: "))
b = int(input("Second positive integer: "))

first = a
second = b

while second != 0:
    remainder = first % second
    first = second
    second = remainder

gcd = first
lcm = a * b // gcd
print(lcm)

