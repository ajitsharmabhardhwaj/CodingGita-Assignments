
# Q1. Predict the Loop Values
print("Q1")
for i in range(2, 15, 3):
    print(i)

# Q2. Reverse range() Prediction
print("\nQ2")
for i in range(15, 2, -3):
    print(i)

# Q3. How Many Iterations?
print("\nQ3")
for i in range(4, 31, 5):
    print(i)
# The loop executes 6 times: i = 4, 9, 14, 19, 24, 29.

# Q4. Correct the Boundary
print("\nQ4")
# The stop value is exclusive, so use 19 to include 18.
for i in range(3, 19, 3):
    print(i)

# Q5. Number and Distance from 20
print("\nQ5")
for i in range(5, 11):
    print(i, 20 - i)

# Q6. Number, Square and Cube
print("\nQ6")
for i in range(1, 7):
    print(i, i ** 2, i ** 3)