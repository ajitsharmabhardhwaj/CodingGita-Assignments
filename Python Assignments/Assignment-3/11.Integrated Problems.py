 Answer-59
print("C:\\new\\test")


# Answer-60
name = input("Enter student name: ")
mark1, mark2, mark3 = input("Enter three subject marks: ").split()

mark1 = int(mark1)
mark2 = int(mark2)
mark3 = int(mark3)

total = mark1 + mark2 + mark3
average = total / 3

print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")


# Answer-61
student_id = input("Enter student ID: ")

degree, batch, branch, roll_number = student_id.split("-")
last_three = student_id[-3:]
roll_number = int(roll_number)

print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll Number: {roll_number}")
print("Last three characters:", last_three)


# Answer-62
full_name = input("Enter full name: ")

first_name, middle_name, last_name = full_name.split()

username = first_name.lower() + "." + last_name.lower()

print(username)


# Answer-63
sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Number of words: {len(words)}")


# Answer-64
email = input("Enter email address: ")

print("@ Present:", "@" in email)

username, domain = email.split("@")

print("Username:", username)
print("Domain:", domain)


# Answer-65
character = input("Enter one character: ")

code = ord(character)
previous_character = chr(code - 1)
next_character = chr(code + 1)

print(f"Character: {character}")
print(f"Code: {code}")
print(f"Previous: {previous_character}")
print(f"Next: {next_character}")


# Answer-66
product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
discount_percentage = float(input("Enter discount percentage: "))

subtotal = price * quantity
discount = subtotal * discount_percentage / 100
final_total = subtotal - discount

print(f"Product: {product}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")


# Answer-67
date = input("Enter date (DD-MM-YYYY): ")

day, month, year = date.split("-")

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
print("Year using slicing:", date[-4:])


# Answer-68
text = input("Enter two words: ")

first_word, second_word = text.split()

print(f"First Word: {first_word}")
print(f"Second Word: {second_word}")
print(f"First Word Reversed: {first_word[::-1]}")
print(f"Second Word Reversed: {second_word[::-1]}")


# Answer-69
student_code = input("Enter student code: ")

degree, batch, branch, roll = student_code.split("-")

print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll: {roll[-3:]}")
print(f"Code: {degree}/{branch}/{roll[-3:]}")


# Answer-70
full_name = input("Enter full name: ")

first_name, middle_name, last_name = full_name.split()

first_name_upper_part = first_name[:3].upper()
last_name_lower_part = last_name[1:4]
reversed_name = full_name[::-1]

print(f"Original: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_name_upper_part}")
print(f"Last Name (Lower Part): {last_name_lower_part}")
print(f"Full Name Reversed: {reversed_name}")


