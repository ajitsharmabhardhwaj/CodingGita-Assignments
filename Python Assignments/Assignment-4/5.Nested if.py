# Q36. Login with Role
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "admin123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")


# Q37. Driving License Eligibility
age = int(input("Enter age: "))
test_status = input("Enter test status: ")

if age >= 18:
    if test_status == "pass":
        print("License Approved")
    else:
        print("Test Not Passed")
else:
    print("Age Not Eligible")


# Q38. ATM Withdrawal
balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount % 100 == 0:
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")


# Q39. Exam Result with Attendance
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if attendance >= 75:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")


# Q40. Bank Account Verification
account_type = input("Enter account type: ")
balance = float(input("Enter balance: "))

if account_type == "savings":
    if balance >= 1000:
        print("Minimum Balance Maintained")
    else:
        print("Minimum Balance Not Maintained")
else:
    print("Unsupported Account")


# Q41. Online Shopping Eligibility
amount = float(input("Enter order amount: "))
payment_method = input("Enter payment method: ")

if amount >= 500:
    if payment_method == "card":
        print("Card Payment Accepted")
    elif payment_method == "upi":
        print("UPI Payment Accepted")
    else:
        print("Unsupported Payment Method")
else:
    print("Minimum Order Amount Not Reached")


# Q42. Hostel Room Allocation
year = int(input("Enter year of study: "))
attendance = int(input("Enter attendance: "))

if year == 2 or year == 3 or year == 4:
    if attendance >= 75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")


# Q43. Internet Plan Upgrade
plan = input("Enter current plan: ")
usage = float(input("Enter monthly usage in GB: "))

if plan == "basic":
    if usage > 100:
        print("Recommend Upgrade")
    else:
        print("Basic Plan Is Sufficient")
else:
    print("Already on Higher Plan")
