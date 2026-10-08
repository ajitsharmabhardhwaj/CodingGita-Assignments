# Q62. Daily Expense Analyzer
days = int(input("Enter number of days: "))
total = 0
highest = 0
lowest = 0

for i in range(1, days + 1):
    expense = float(input("Enter expense: "))
    total = total + expense

    if i == 1:
        highest = expense
        lowest = expense
    else:
        if expense > highest:
            highest = expense

        if expense < lowest:
            lowest = expense

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)


# Q63. Student Marks Analyzer
subjects = int(input("Enter number of subjects: "))
total = 0
highest = 0
lowest = 0

for i in range(1, subjects + 1):
    marks = float(input("Enter marks: "))
    total = total + marks

    if i == 1:
        highest = marks
        lowest = marks
    else:
        if marks > highest:
            highest = marks

        if marks < lowest:
            lowest = marks

average = total / subjects

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)


# Q64. Attendance Analyzer
days = int(input("Enter working days: "))
present = 0
absent = 0

for i in range(1, days + 1):
    status = input("Enter status (P/A): ")

    if status == "P":
        present = present + 1
    elif status == "A":
        absent = absent + 1

attendance = present / days * 100

print("Present:", present)
print("Absent:", absent)
print("Attendance:", round(attendance, 2), "%")


# Q65. Electricity Usage Analyzer
days = int(input("Enter number of days: "))
total = 0
above_10 = 0

for i in range(1, days + 1):
    units = int(input("Enter units: "))
    total = total + units

    if units > 10:
        above_10 = above_10 + 1

print("Total Units:", total)
print("Days Above 10:", above_10)


# Q66. Shopping Bill Analyzer
products = int(input("Enter number of products: "))
total = 0
above_1000 = 0

for i in range(1, products + 1):
    price = float(input("Enter price: "))
    total = total + price

    if price > 1000:
        above_1000 = above_1000 + 1

print("Total Bill:", total)
print("Products Above 1000:", above_1000)


# Q67. Login Attempt Analyzer
attempts = int(input("Enter number of attempts: "))
successful = 0
failed = 0

for i in range(1, attempts + 1):
    status = input("Enter attempt status: ")

    if status == "success":
        successful = successful + 1
    elif status == "failed":
        failed = failed + 1

success_rate = successful / attempts * 100

print("Successful:", successful)
print("Failed:", failed)
print("Success Rate:", success_rate, "%")
