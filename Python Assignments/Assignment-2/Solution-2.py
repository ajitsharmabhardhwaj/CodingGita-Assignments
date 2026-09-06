# type_conversions_answers.py
# Answers for Questions 1 — 10 (conversion exercises)

# --- Question 1: String to Integer ---
age = "25"
age_int = int(age)
print("Q1:")
print(age_int)
print(type(age_int))
print()  # blank line

# --- Question 2: String to Float ---
marks = "75.5"
marks_float = float(marks)
print("Q2:")
print(marks_float)
print(type(marks_float))
print()

# --- Question 3: Integer to Float ---
number = 50
number_float = float(number)
print("Q3:")
print(number_float)
print(type(number_float))
print()

# --- Question 4: Float to Integer ---
marks = 85.9
marks_int = int(marks)   # decimal part will be truncated
print("Q4:")
print(marks_int)
print(type(marks_int))
print()  # note: decimal part .9 is dropped (truncated)

# --- Question 5: Integer to String ---
roll_number = 101
roll_str = str(roll_number)
print("Q5:")
print(roll_str)
print(type(roll_str))
print()

# --- Question 6: Multiple Conversions ---
v1 = int("18")
v2 = float("92.5")
v3 = str(100)
v4 = int(45.8)   # decimal truncated -> 45
print("Q6:")
print(v1, type(v1))
print(v2, type(v2))
print(v3, type(v3))
print(v4, type(v4))
print()

# --- Question 7: Predict the Output (then run it) ---
print("Q7 (predicted):")
print("b -> 20")
print("d -> 10")
print("f -> '25'")
print("types -> <class 'int'>, <class 'int'>, <class 'str'>")
print()
# Now actual code:
a = "20"
b = int(a)

c = 10.8
d = int(c)

e = 25
f = str(e)

print("Q7 (actual run):")
print(b)
print(d)
print(f)
print(type(b))
print(type(d))
print(type(f))
print()

# --- Question 8: Debug Type Casting ---
# Original buggy code:
# age = "19"
# new_age = age + 1   # error: can't add int to str
# Correct version:
age = "19"
new_age = int(age) + 1
print("Q8:")
print("Age:", new_age)
print()

# --- Question 9: Marks Conversion ---
marks = "85"
final_marks = int(marks) + 5
print("Q9:")
print("Final Marks:", final_marks)
print()

# --- Question 10: Price Conversion ---
price = "1499.50"
total_amount = float(price) + 99.50
print("Q10:")
print("Total Amount:", total_amount)
print()

# arithmetic_answers.py
# Answers for Questions 11 — 20 (arithmetic operator exercises)

# --- Question 11: Basic Arithmetic ---
a = 20
b = 6
print("Q11 — Basic Arithmetic (a=20, b=6):")
print("Addition:         ", a + b)
print("Subtraction:      ", a - b)
print("Multiplication:   ", a * b)
print("Division (float): ", a / b)
print("Floor division:   ", a // b)
print("Remainder:        ", a % b)
print("Power (a ** b):   ", a ** b)
print()

# --- Question 12: Predict the Output ---
a = 17
b = 5
print("Q12 — Predict the Output (a=17, b=5):")
print("a / b  ->", a / b)   # float division
print("a // b ->", a // b)  # floor division
print("a % b  ->", a % b)   # remainder
print("Explanation: '/' gives true division (float). '//' gives integer quotient (floor). '%' gives leftover remainder.")
print()

# --- Question 13: Operator Precedence ---
result = 10 + 5 * 2
print("Q13 — Operator Precedence:")
print("10 + 5 * 2 =", result)
print("If you want addition first: (10 + 5) * 2 =", (10 + 5) * 2)
print()

# --- Question 14: More Precedence Practice ---
result = 20 - 4 * 3 + 2
print("Q14 — More Precedence Practice:")
print("20 - 4 * 3 + 2 =", result)
print("Make order explicit with parentheses: (20 - (4 * 3)) + 2 =", (20 - (4 * 3)) + 2)
print()

# --- Question 15: Power Operator ---
print("Q15 — Power Operator:")
print("2 ** 3 =", 2 ** 3)
print("3 ** 2 =", 3 ** 2)
print("10 ** 2 =", 10 ** 2)
side = 5
area_square = side ** 2
print("side = 5 -> area of square = side ** 2 =", area_square)
print()

# --- Question 16: Shopping Bill ---
notebook = 80
pen = 20
pencil = 10
total = notebook + pen + pencil
print("Q16 — Shopping Bill:")
print("Total Amount:", total)
print()

# --- Question 17: Multiple Quantities ---
notebook_price = 50
pen_price = 15
calc_price = 500
notebook_cost = 3 * notebook_price
pen_cost = 2 * pen_price
calc_cost = 1 * calc_price
total_bill = notebook_cost + pen_cost + calc_cost
print("Q17 — Multiple Quantities:")
print("Notebook Cost:    ", notebook_cost)
print("Pen Cost:         ", pen_cost)
print("Calculator Cost:  ", calc_cost)
print("Total Bill:       ", total_bill)
print()

# --- Question 18: Complete Groups and Remainder ---
students = 47
group_size = 5
complete_groups = students // group_size
students_left = students % group_size
print("Q18 — Complete Groups and Remainder:")
print("Complete Groups:", complete_groups)
print("Students Left:  ", students_left)
print()

# --- Question 19: Average Marks ---
python_marks = 85
math_marks = 78
physics_marks = 92
total_marks = python_marks + math_marks + physics_marks
average = total_marks / 3
print("Q19 — Average Marks:")
print("Total Marks:  ", total_marks)
print("Average Marks:", average)
print()

# --- Question 20: Percentage ---
eng = 78
math = 85
py = 92
phys = 81
chem = 74
total = eng + math + py + phys + chem
max_total = 5 * 100
percentage = (total / max_total) * 100
print("Q20 — Percentage:")
print("Total Marks: ", total, "/", max_total)
print("Percentage:  ", percentage, "%")
print()

# digit_extraction_answers.py
# Answers for Q21 - Q35 (digit extraction problems)
# Uses only arithmetic (% and //) for digit extraction.

def q21_ones_digit():
    number = 583
    ones = number % 10
    print("Q21 — Ones Digit:")
    print("Ones Digit:", ones)
    print()

def q22_tens_digit():
    number = 583
    tens = (number // 10) % 10
    print("Q22 — Tens Digit:")
    print("Tens Digit:", tens)
    print()

def q23_hundreds_digit():
    number = 583
    hundreds = (number // 100) % 10  # or number // 100
    print("Q23 — Hundreds Digit:")
    print("Hundreds Digit:", hundreds)
    print()

def q24_three_digit_analyzer():
    number = 746
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    print("Q24 — Three-Digit Number Analyzer (number = 746):")
    print("Ones Digit:", ones)
    print("Tens Digit:", tens)
    print("Hundreds Digit:", hundreds)
    print()

def q25_four_digit_number():
    number = 5829
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    print("Q25 — Four-Digit Number (number = 5829):")
    print("Ones Digit:", ones)
    print("Tens Digit:", tens)
    print("Hundreds Digit:", hundreds)
    print("Thousands Digit:", thousands)
    print()

def q26_sum_of_digits():
    number = 583
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    total = ones + tens + hundreds
    print("Q26 — Sum of Digits (number = 583):")
    print("Sum of Digits:", total)
    print()

def q27_four_digit_sum():
    number = 4726
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    total = ones + tens + hundreds + thousands
    print("Q27 — Four-Digit Sum (number = 4726):")
    print("Sum of Digits:", total)
    print()

def q28_product_of_digits():
    number = 234
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    product = ones * tens * hundreds
    print("Q28 — Product of Digits (number = 234):")
    print("Product of Digits:", product)
    print()

def q29_reverse_three_digit():
    number = 583
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    reversed_num = ones * 100 + tens * 10 + hundreds
    print("Q29 — Reverse a Three-Digit Number:")
    print("Original Number:", number)
    print("Reversed Number:", reversed_num)
    print()

def q30_reverse_four_digit():
    number = 4726
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    reversed_num = ones * 1000 + tens * 100 + hundreds * 10 + thousands
    print("Q30 — Reverse a Four-Digit Number:")
    print("Original Number:", number)
    print("Reversed Number:", reversed_num)
    print()

def q31_place_value():
    number = 5834
    thousands_digit = (number // 1000) % 10
    hundreds_digit = (number // 100) % 10
    tens_digit = (number // 10) % 10
    ones_digit = number % 10
    print("Q31 — Place Value (number = 5834):")
    print("Thousands Place:", thousands_digit * 1000)
    print("Hundreds Place:", hundreds_digit * 100)
    print("Tens Place:", tens_digit * 10)
    print("Ones Place:", ones_digit)
    print()

def q32_difference_first_last():
    number = 583
    hundreds = (number // 100) % 10
    ones = number % 10
    diff = hundreds - ones
    print("Q32 — Difference Between First and Last Digit (number = 583):")
    print("Difference:", diff)
    print()

def q33_debug_digit_extraction():
    # buggy code:
    # number = 583
    # ones = number / 10   # wrong: / gives float and is not last digit
    # print("Ones Digit:", ones)
    # Correct version:
    number = 583
    ones = number % 10
    print("Q33 — Debug Digit Extraction (fixed):")
    print("Ones Digit:", ones)
    print()

def q34_four_digit_extraction():
    number = 9365
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    print("Q34 — Four-Digit Extraction (number = 9365):")
    print("Thousands Digit:", thousands)
    print("Hundreds Digit:", hundreds)
    print("Tens Digit:", tens)
    print("Ones Digit:", ones)
    print()

def q35_build_number():
    hundreds = 5
    tens = 8
    ones = 3
    number = hundreds * 100 + tens * 10 + ones
    print("Q35 — Build a Number from digits (hundreds=5,tens=8,ones=3):")
    print("Number:", number)
    print()

# Run all
if __name__ == "__main__":
    q21_ones_digit()
    q22_tens_digit()
    q23_hundreds_digit()
    q24_three_digit_analyzer()
    q25_four_digit_number()
    q26_sum_of_digits()
    q27_four_digit_sum()
    q28_product_of_digits()
    q29_reverse_three_digit()
    q30_reverse_four_digit()
    q31_place_value()
    q32_difference_first_last()
    q33_debug_digit_extraction()
    q34_four_digit_extraction()
    q35_build_number()

# real_life_arithmetic.py
# Answers for Questions 36 — 44 (real-life arithmetic problems)

def q36_simple_interest():
    principal = 10000
    rate = 5     # percent
    time = 2     # years
    simple_interest = (principal * rate * time) / 100
    print("Q36 — Simple Interest:")
    print("Simple Interest:", simple_interest)
    print()

def q37_rectangle():
    length = 15  # cm
    width = 8    # cm
    area = length * width
    perimeter = 2 * (length + width)
    print("Q37 — Rectangle:")
    print("Area:", area)
    print("Perimeter:", perimeter)
    print()

def q38_circle():
    r = 7
    pi = 3.14
    area = pi * r * r
    print("Q38 — Circle:")
    print("Area:", area)
    print()

def q39_temperature_conversion():
    celsius = 35
    fahrenheit = (celsius * 9 / 5) + 32
    print("Q39 — Temperature Conversion:")
    print(f"{celsius}°C -> {fahrenheit}°F")
    print()

def q40_time_conversion():
    total_seconds = 367
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    print("Q40 — Time Conversion:")
    print("Minutes:", minutes)
    print("Seconds:", seconds)
    print()

def q41_hms_conversion():
    total_seconds = 7384
    hours = total_seconds // 3600
    rem = total_seconds % 3600
    minutes = rem // 60
    seconds = rem % 60
    print("Q41 — Hours, Minutes and Seconds:")
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)
    print()

def q42_salary():
    basic = 25000
    hra = 5000
    travel_allowance = 2500
    tax_deduction = 3000
    gross = basic + hra + travel_allowance
    net = gross - tax_deduction
    print("Q42 — Salary Calculation:")
    print("Gross Salary:", gross)
    print("Net Salary:", net)
    print()

def q43_travel_cost():
    distance_km = 120
    km_per_litre = 20
    price_per_litre = 100
    fuel_required = distance_km / km_per_litre
    total_cost = fuel_required * price_per_litre
    print("Q43 — Travel Cost:")
    print("Fuel required (litres):", fuel_required)
    print("Total fuel cost:", total_cost)
    print()

def q44_shopping_discount():
    price = "2500"
    discount = "10"   # percent as string
    # convert to numeric
    price_num = float(price)
    discount_pct = float(discount)
    discount_amount = (price_num * discount_pct) / 100
    final_price = price_num - discount_amount
    print("Q44 — Shopping Discount:")
    print("Discount amount:", discount_amount)
    print("Final price:", final_price)
    print()

if __name__ == "__main__":
    q36_simple_interest()
    q37_rectangle()
    q38_circle()
    q39_temperature_conversion()
    q40_time_conversion()
    q41_hms_conversion()
    q42_salary()
    q43_travel_cost()
    q44_shopping_discount()

# type_casting_arithmetic_answers.py
# Solutions for Questions 45 - 50

def q45_string_numbers():
    price = "1200"
    quantity = "4"
    price_num = int(price)
    qty_num = int(quantity)
    total_price = price_num * qty_num
    print("Q45 — String Numbers:")
    print("Price:", price_num)
    print("Quantity:", qty_num)
    print("Total Price:", total_price)
    print()

def q46_student_result():
    python_marks = "85"
    math_marks = "78"
    physics_marks = "91"
    py = int(python_marks)
    ma = int(math_marks)
    ph = int(physics_marks)
    total = py + ma + ph
    average = total / 3
    print("Q46 — Student Result:")
    print("Total Marks:", total)
    print("Average Marks:", average)
    print()

def q47_bill_with_tax():
    price = "1500"
    quantity = "2"
    tax_rate = "5"
    price_num = float(price)
    qty_num = int(quantity)
    tax_pct = float(tax_rate)
    subtotal = price_num * qty_num
    tax_amount = subtotal * tax_pct / 100
    final_bill = subtotal + tax_amount
    print("Q47 — Bill with Tax:")
    print("Subtotal:", subtotal)
    print("Tax amount:", tax_amount)
    print("Final bill:", final_bill)
    print()

def q48_discount_and_gst():
    price = 2000.0
    discount_pct = 15.0
    gst_pct = 18.0
    discount_amount = price * discount_pct / 100
    price_after_discount = price - discount_amount
    gst_amount = price_after_discount * gst_pct / 100
    final_price = price_after_discount + gst_amount
    print("Q48 — Discount + GST:")
    print("Discount amount:", discount_amount)
    print("Price after discount:", price_after_discount)
    print("GST amount:", gst_amount)
    print("Final price:", final_price)
    print()

def q49_debug_billing_program():
    # Buggy original:
    # price = "500"
    # quantity = 3
    # total = price + quantity            # wrong: string + int, also should multiply
    # Corrected version:
    price = "500"
    quantity = 3
    price_num = int(price)
    total = price_num * quantity
    print("Q49 — Debug the Billing Program (fixed):")
    print("Total:", total)
    print()

def q50_debug_marks_program():
    # Buggy original:
    # marks1 = "80"
    # marks2 = "75"
    # marks3 = "90"
    # total = marks1 + marks2 + marks3   # wrong: string concatenation
    # Corrected:
    marks1 = "80"
    marks2 = "75"
    marks3 = "90"
    m1 = int(marks1)
    m2 = int(marks2)
    m3 = int(marks3)
    total = m1 + m2 + m3
    print("Q50 — Debug the Marks Program (fixed):")
    print("Total Marks:", total)
    print()

if __name__ == "__main__":
    q45_string_numbers()
    q46_student_result()
    q47_bill_with_tax()
    q48_discount_and_gst()
    q49_debug_billing_program()
    q50_debug_marks_program()

# q51_55_answers.py
# Q51 - Q55: Predictions shown as actual outputs (type-casting, arithmetic, parentheses, digit extraction)

def q51_type_casting_output():
    a = "50"
    b = int(a)
    print("Q51 — Type Casting Output")
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    print()  # blank line

def q52_float_to_int():
    number = 99.99
    result = int(number)
    print("Q52 — Float to Integer")
    print(number)
    print(result)
    print("Note: int() truncates the decimal portion (does not round).")
    print()

def q53_arithmetic_output():
    a = 12
    b = 5
    print("Q53 — Arithmetic Output")
    print(a + b)   # addition
    print(a - b)   # subtraction
    print(a * b)   # multiplication
    print(a / b)   # true division (float)
    print(a // b)  # floor division
    print(a % b)   # remainder
    print()

def q54_parentheses_challenge():
    print("Q54 — Parentheses Challenge")
    print(10 + 5 * 2)        # multiplication before addition
    print((10 + 5) * 2)      # parentheses force addition first
    print(20 / 5 + 3)        # left-to-right after division
    print(20 / (5 + 3))      # parentheses change denominator
    print("Note: parentheses change evaluation order (operator precedence).")
    print()

def q55_digit_challenge():
    number = 684
    a = number % 10          # ones
    b = number // 10
    c = b % 10               # tens
    d = number // 100        # hundreds
    print("Q55 — Digit Challenge")
    print(a)   # ones
    print(c)   # tens
    print(d)   # hundreds
    print("Identification: a = ones, c = tens, d = hundreds.")
    print()

if __name__ == "__main__":
    q51_type_casting_output()
    q52_float_to_int()
    q53_arithmetic_output()
    q54_parentheses_challenge()
    q55_digit_challenge()

# mixed_debugging_answers.py
# Answers for Q56 - Q60 (Mixed Debugging + final challenge)
# Each section prints the corrected result and matches the expected outputs.

def q56_debug_student_program():
    # Corrected version of the buggy student program
    student_name = "Ravi"
    marks = "85"

    # convert marks to int before arithmetic
    total = int(marks) + 5

    print("Q56 — Debug the Student Program (fixed):")
    print("Student:", student_name)    # fixed variable name capitalization
    print("Marks:", total)
    print("Type:", type(total))
    print()

def q57_debug_number_program():
    # Original intention: print ones, tens, hundreds of 746
    number = 746

    ones = number % 10
    tens = (number // 10) % 10
    hundreds = number // 100

    print("Q57 — Debug the Number Program (fixed):")
    print("Ones:", ones)
    print("Tens:", tens)
    print("Hundreds:", hundreds)
    print()

def q58_debug_discount_program():
    # Fix: convert strings to numbers first
    price = "2000"
    discount = "15"

    price_num = float(price)
    discount_pct = float(discount)
    discount_amount = price_num * discount_pct / 100
    final_price = price_num - discount_amount

    print("Q58 — Debug the Discount Program (fixed):")
    print("Discount:", discount_amount)
    print("Final Price:", final_price)
    print()

def q59_complete_debugging_challenge():
    # Correct full program (fixed parsing, arithmetic, names, parentheses)
    student_name = "Rahul"
    marks1 = "85"
    marks2 = "90"
    marks3 = "78"

    m1 = int(marks1)
    m2 = int(marks2)
    m3 = int(marks3)

    total = m1 + m2 + m3
    average = total / 3

    print("Q59 — Complete Debugging Challenge (fixed):")
    print("Student:", student_name)
    print("Total Marks:", total)
    print("Average:", average)
    print("Marks Type:", type(total))
    print()

def q60_final_challenge_number_and_billing():
    # Part A — Number Analysis for number = 5836
    number = 5836
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    sum_digits = ones + tens + hundreds + thousands
    reversed_number = ones * 1000 + tens * 100 + hundreds * 10 + thousands

    print("Q60 — Part A: Number Analysis (number = 5836)")
    print("Thousands digit:", thousands)
    print("Hundreds digit:", hundreds)
    print("Tens digit:", tens)
    print("Ones digit:", ones)
    print("Sum of digits:", sum_digits)
    print("Reversed number:", reversed_number)
    print()

    # Part B — Product Billing
    price = "1250"
    quantity = "4"
    discount = "10"   # percent

    price_num = float(price)
    qty_num = int(quantity)
    discount_pct = float(discount)

    subtotal = price_num * qty_num
    discount_amount = subtotal * discount_pct / 100
    final_amount = subtotal - discount_amount

    print("Q60 — Part B: Product Billing")
    print("Subtotal:", subtotal)
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)
    print()

if __name__ == "__main__":
    q56_debug_student_program()
    q57_debug_number_program()
    q58_debug_discount_program()
    q59_complete_debugging_challenge()
    q60_final_challenge_number_and_billing()

print("")

