Q71. Condition Order
Code:
marks = 85


if marks >= 40:
    print("Pass")
elif marks >= 75:
    print("Very Good")
else:
    print("Fail")
Answer:
85 → Pass
Explanation:

85 >= 40 already True hai. Python pehle if condition ko check karta hai, isliye "Pass" print hota hai. Uske baad elif check nahi hota.

Q72. Correct the Condition Order
Code:
marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
Output:
95 → A
85 → B
50 → Pass
30 → Fail
Explanation:

Conditions ko highest range se lowest range mein check karna chahiye. Python jo pehli true condition milti hai, uska block execute karta hai aur baaki conditions skip kar deta hai.

Q73. Nested if Execution Flow
Given:
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")
Test Case 1:
age = 20
has_id = True
Output:
Entry Allowed
Test Case 2:
age = 20
has_id = False
Output:
ID Required
Test Case 3:
age = 16
has_id = True
Output:
Underage
Explanation:

Pehle age >= 18 check hota hai. Agar age 18 ya usse zyada hai, tab has_id check hota hai.

Q74. match-case and Default Case
Code:
choice = 5

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid Choice")
Test Cases:
1 → Add
3 → Delete
5 → Invalid Choice
Purpose of case _:

case _ default case hai. Jab koi bhi previous case match nahi hota, case _ execute hota hai.

Q75. Final Execution Challenge
Code:
marks = 82
attendance = 80

if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")
Test Cases:
82 80 → Grade B
92 80 → Grade A
55 80 → Pass
92 60 → Not Eligible
