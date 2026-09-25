Q69. Debug the Condition

Correct Code:
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
Test Cases:
20 → Eligible
15 → Not Eligible
Q70. Debug the Nested Condition

Correct Code:
marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    else:
        print("Pass")
else:
    print("Fail")
Test Cases:
95 → A
80 → B
50 → Pass
30 → Fail
