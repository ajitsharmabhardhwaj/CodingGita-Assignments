# Q44. Greatest of Three Numbers
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a == b and b == c:
    print("All are Equal")
elif a == b and a > c:
    print("A and B are Equal and Greatest")
elif a == c and a > b:
    print("A and C are Equal and Greatest")
elif b == c and b > a:
    print("B and C are Equal and Greatest")
elif a > b:
    if a > c:
        print("A is Greatest")
    else:
        print("C is Greatest")
else:
    if b > c:
        print("B is Greatest")
    else:
        print("C is Greatest")


# Q45. Student Result with Grade
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Not Eligible")


# Q46. Employee Bonus
salary = float(input("Enter salary: "))
rating = int(input("Enter performance rating: "))

if salary >= 30000:
    if rating == 5:
        print("Bonus: 20%")
    elif rating == 4:
        print("Bonus: 15%")
    elif rating == 3:
        print("Bonus: 10%")
    else:
        print("Bonus: 5%")
else:
    print("Not Eligible for Bonus")


# Q47. Bus Ticket Category
age = int(input("Enter age: "))
distance = float(input("Enter distance in km: "))

if age < 5:
    print("Free")
elif age >= 60:
    print("Senior")
else:
    if distance <= 10:
        print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")


# Q48. Product Purchase Validation
stock = int(input("Enter stock: "))
payment_status = input("Enter payment status: ")

if stock > 0:
    if payment_status == "paid":
        print("Order Confirmed")
    elif payment_status == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")


# Q49. Travel Ticket Validation
age = int(input("Enter age: "))
ticket_type = input("Enter ticket type: ")

if age < 5:
    print("Free Travel")
elif age >= 60:
    print("Senior Passenger")
else:
    if ticket_type == "AC":
        print("AC Ticket")
    elif ticket_type == "Sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")

