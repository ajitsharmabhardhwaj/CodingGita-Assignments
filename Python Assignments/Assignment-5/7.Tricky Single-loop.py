# Q53. Second Largest Digit
n = int(input("Enter number: "))
temp = n
largest = -1
second = -1

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10

        if digit > largest:
            second = largest
            largest = digit
        elif digit > second and digit != largest:
            second = digit

        temp = temp // 10

print(second)


# Q54. Longest Consecutive Equal Character Run
text = input("Enter string: ")
current = 0
best = 0
previous = ""

for character in text:
    if character == previous:
        current = current + 1
    else:
        current = 1
        previous = character

    if current > best:
        best = current

print(best)


# Q55. Most Frequent Character - Controlled Approach
text = input("Enter string: ")
target = input("Enter target character: ")
count = 0
length = 0

for character in text:
    length = length + 1

    if character == target:
        count = count + 1

frequency = count / length * 100

print("Count =", count)
print("Frequency =", round(frequency, 2), "%")


# Q56. Running Digit Sum Until the End
n = int(input("Enter number: "))
temp = n
total = 0

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10
        total = total + digit
        print(total)
        temp = temp // 10


# Q57. Number with Most Even Digits
n = int(input("Enter number: "))
temp = n
even = 0
odd = 0

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10

        if digit % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1

        temp = temp // 10

if even > odd:
    print("More Even Digits")
elif odd > even:
    print("More Odd Digits")
else:
    print("Equal")


# Q58. Alternating Digit Sum
n = int(input("Enter number: "))
temp = n
total = 0
sign = 1

for i in range(1, n + 1):
    if temp > 0:
        digit = temp % 10
        total = total + digit * sign
        sign = sign * -1
        temp = temp // 10

print(total)


# Q59. Output Prediction - Accumulator Trap
total = 0

for i in range(1, 6):
    total = total + i * 2
    print(total)


# Q60. Output Prediction - Condition Inside Loop
count = 0

for i in range(1, 11):
    if i % 2 == 0:
        count = count + 1

print(count)


# Q61. Debug the Accumulator
total = 0

for i in range(1, 6):
    total = total + i

print(total)
