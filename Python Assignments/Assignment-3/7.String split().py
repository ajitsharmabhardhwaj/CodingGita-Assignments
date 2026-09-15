# Answer-33
text = "Python is easy"

print(text.split())


# Answer-34
data = "apple,banana,mango"

print(data.split(","))


# Answer-35
text = "Python is easy"

print(text.split(","))


# Answer-36
full_name = input("Enter full name: ")

first_name, middle_name, last_name = full_name.split()

print(first_name)
print(middle_name)
print(last_name)


# Answer-37
first_name, last_name = input("Enter first and last name: ").split()

print("First Name:", first_name)
print("Last Name:", last_name)


# Answer-38
a, b, c = input("Enter three integers: ").split()

a = int(a)
b = int(b)
c = int(c)

print(a + b + c)


# Answer-39
data = input("Enter student record: ")

name, age, course, city = data.split(",")

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("City:", city)


# Answer-40
email = input("Enter email address: ")

username, domain = email.split("@")

print("Username:", username)
print("Domain:", domain)


# Answer-41
sentence = input("Enter a sentence: ")

words = sentence.split()

print("First word:", words[0])
print("Last word:", words[-1])
print("Total words:", len(words))

