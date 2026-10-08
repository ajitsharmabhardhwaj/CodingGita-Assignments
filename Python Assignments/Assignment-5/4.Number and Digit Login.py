# Q23. Count Digits Using a Loop
n = int(input("Enter number: "))
temp = n
count = 0

for i in range(1, n + 1):
    if temp > 0:
        count = count + 1
        temp = temp // 10

print(count)


# Q24. Sum of Digits
n = int(input("Enter number: "))
temp = n
total = 0

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10
        total = total + digit
        temp = temp // 10

print(total)


# Q25. Product of Digits
n = int(input("Enter number: "))
temp = n
product = 1

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10
        product = product * digit
        temp = temp // 10

print(product)


# Q26. Count Even Digits
n = int(input("Enter number: "))
temp = n
count = 0

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10

        if digit % 2 == 0:
            count = count + 1

        temp = temp // 10

print(count)


# Q27. Sum of Even Digits
n = int(input("Enter number: "))
temp = n
total = 0

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10

        if digit % 2 == 0:
            total = total + digit

        temp = temp // 10

print(total)


# Q28. Largest Digit Without max()
n = int(input("Enter number: "))
temp = n
largest = 0

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10

        if digit > largest:
            largest = digit

        temp = temp // 10

print(largest)


# Q29. Smallest Digit Without min()
n = int(input("Enter number: "))
temp = n
smallest = 9

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10

        if digit < smallest:
            smallest = digit

        temp = temp // 10

print(smallest)


# Q30. Reverse a Number
n = int(input("Enter number: "))
temp = n
reverse = 0

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

print(reverse)


# Q31. Palindrome Number
n = int(input("Enter number: "))
temp = n
reverse = 0

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

if reverse == n:
    print("Palindrome")
else:
    print("Not Palindrome")


# Q32. Count a Specific Digit
n = int(input("Enter number: "))
target = int(input("Enter target digit: "))
temp = n
count = 0

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10

        if digit == target:
            count = count + 1

        temp = temp // 10

print(count)


# Q33. First Digit Using Repeated Division
n = int(input("Enter number: "))
temp = n

for i in range(1, n + 1):
    if temp >= 10:
        temp = temp // 10

print(temp)


# Q34. Difference Between Largest and Smallest Digit
n = int(input("Enter number: "))
temp = n
largest = 0
smallest = 9

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10

        if digit > largest:
            largest = digit

        if digit < smallest:
            smallest = digit

        temp = temp // 10

print(largest - smallest)


# Q35. Digit Position Value
n = int(input("Enter number: "))
temp = n
position = 1

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10
        print(digit, position)
        position = position + 1
        temp = temp // 10


# Q36. Armstrong Number - 3 Digit
n = int(input("Enter 3-digit number: "))
temp = n
total = 0

for i in range(3):
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

