# Q1. Positive Number
number = int(input("Enter a number: "))
if number > 0:
    print("Positive Number")


# Q2. Voting Eligibility Check
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to Vote")


# Q3. Temperature Warning
temperature = float(input("Enter temperature: "))
if temperature > 40:
    print("High Temperature")


# Q4. Divisible by 5
number = int(input("Enter an integer: "))
if number % 5 == 0:
    print("Divisible by 5")


# Q5. Free Delivery
amount = float(input("Enter order amount: "))
if amount >= 1000:
    print("Free Delivery")


# Q6. Character Check
character = input("Enter a character: ")
if character == "A":
    print("You entered A")


# Q7. Password Length Check
password = input("Enter password: ")
if len(password) >= 8:
    print("Strong Length")


# Q8. Number of Digits
number = int(input("Enter an integer: "))
if number >= 100 and number <= 999:
    print("Three Digit Number")
