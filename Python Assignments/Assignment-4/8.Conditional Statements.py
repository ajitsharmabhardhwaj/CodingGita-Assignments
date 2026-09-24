# Q58. Student ID Validation
student_id = input("Enter student ID: ")
parts = student_id.split("-")
degree = parts[0]
batch = parts[1]
branch = parts[2]
roll_number = parts[3]

if branch == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")


# Q59. Email Domain Checker
email = input("Enter email address: ")
parts = email.split("@")
domain = parts[1]

if domain == "gmail.com":
    print("Gmail User")
else:
    print("Other Email Provider")


# Q60. Username Generator Validation
full_name = input("Enter full name: ")
parts = full_name.split(" ")
username = parts[0].lower() + "." + parts[2].lower()

if "." in username:
    print("Valid Username Format")
else:
    print("Invalid Username Format")


# Q61. Number Digit Analyzer
number = int(input("Enter a positive integer: "))

if number >= 0 and number <= 9:
    print("One Digit")
elif number <= 99:
    print("Two Digits")
elif number <= 999:
    print("Three Digits")
else:
    print("Four or More Digits")


# Q62. Shopping Bill Category
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity

if subtotal >= 5000:
    discount = 20
elif subtotal >= 2000:
    discount = 10
else:
    discount = 0

discount_amount = subtotal * discount / 100
final_amount = subtotal - discount_amount

print(f"Subtotal: {subtotal:.0f}, Discount: {discount}%, Final: {final_amount:.2f}")


# Q63. Electricity Bill Category
units = int(input("Enter units consumed: "))

if units <= 100:
    rate = 5
elif units <= 300:
    rate = 7
else:
    rate = 10

bill = units * rate

print(f"Units: {units}")
print(f"Rate: ₹{rate}")
print(f"Bill: ₹{bill}")


# Q64. ATM Menu
balance = 10000
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print(f"Balance: {balance}")
    case 2:
        deposit = float(input("Enter deposit amount: "))
        balance = balance + deposit
        print(f"Deposit Successful, Balance: {balance:g}")
    case 3:
        withdrawal = float(input("Enter withdrawal amount: "))
        if withdrawal <= balance:
            balance = balance - withdrawal
            print(f"Withdrawal Successful, Balance: {balance:g}")
        else:
            print("Insufficient Balance")
    case 4:
        print("Exit")
    case _:
        print("Invalid Choice")


# Q65. Restaurant Ordering System
choice = int(input("Enter food choice: "))
quantity = int(input("Enter quantity: "))

match choice:
    case 1:
        item = "Pizza"
        price = 250
    case 2:
        item = "Burger"
        price = 150
    case 3:
        item = "Pasta"
        price = 200
    case 4:
        item = "Sandwich"
        price = 120
    case _:
        item = ""
        price = 0

if price == 0:
    print("Invalid Choice")
else:
    total = price * quantity

    if total >= 500:
        discount = total * 10 / 100
    else:
        discount = 0

    final_amount = total - discount

    print(f"Total: {total:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final: {final_amount:.2f}")


# Q66. Exam Result Analyzer
mark1 = float(input("Enter subject 1 marks: "))
mark2 = float(input("Enter subject 2 marks: "))
mark3 = float(input("Enter subject 3 marks: "))
attendance = float(input("Enter attendance: "))

total = mark1 + mark2 + mark3
average = total / 3

if attendance >= 75:
    if average >= 90:
        print("Outstanding")
    elif average >= 75:
        print("Very Good")
    elif average >= 60:
        print("Good")
    elif average >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")


# Q67. Cab Fare Calculator
distance = float(input("Enter distance in km: "))
ride_type = input("Enter ride type: ")

match ride_type:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        rate = 0

if rate == 0:
    print("Invalid Ride Type")
else:
    fare = distance * rate

    if distance > 20:
        fare = fare + (fare * 10 / 100)

    print(f"Fare: {fare:.2f}")


# Q68. College Admission System
score = int(input("Enter entrance score: "))
percentage = float(input("Enter 12th percentage: "))
category = input("Enter category: ")

match category:
    case "general":
        if score >= 80 and percentage >= 75:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")

    case "obc":
        if score >= 70 and percentage >= 70:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")

    case "sc":
        if score >= 60 and percentage >= 60:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")

    case _:
        print("Admission Not Eligible")
