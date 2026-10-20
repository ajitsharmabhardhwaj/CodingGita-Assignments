# Q101. Pairs of Digits with a Target Sum
number = input("Number: ")
target = int(input("Target sum: "))

for first_position in range(len(number)):
    for second_position in range(first_position + 1, len(number)):
        first_digit = int(number[first_position])
        second_digit = int(number[second_position])

        if first_digit + second_digit == target:
            print(first_digit, second_digit)


# Q102. Digit Pairs with a Fixed Difference
number = input("Number: ")
difference = int(input("Difference: "))

for first_position in range(len(number)):
    for second_position in range(first_position + 1, len(number)):
        first_digit = int(number[first_position])
        second_digit = int(number[second_position])

        if abs(first_digit - second_digit) == difference:
            print(first_digit, second_digit)


# Q103. Repeated Digits in a Number
number = input("Number: ")

for position in range(len(number)):
    appeared_before = False
    appears_again = False

    for earlier_position in range(position):
        if number[earlier_position] == number[position]:
            appeared_before = True

    for later_position in range(position + 1, len(number)):
        if number[later_position] == number[position]:
            appears_again = True

    if appears_again and not appeared_before:
        print(number[position])


# Q104. Count Equal Digit Pairs
number = input("Number: ")
pair_count = 0

for first_position in range(len(number)):
    for second_position in range(first_position + 1, len(number)):
        if number[first_position] == number[second_position]:
            pair_count += 1

print(pair_count)


# Q105. Common Characters in Two Strings
first = input("First string: ")
second = input("Second string: ")

for position in range(len(first)):
    appeared_before = False
    occurs_in_second = False

    for earlier_position in range(position):
        if first[earlier_position] == first[position]:
            appeared_before = True

    for character in second:
        if character == first[position]:
            occurs_in_second = True

    if occurs_in_second and not appeared_before:
        print(first[position])


# Q106. Check Whether Two Strings Share a Character
first = input("First string: ")
second = input("Second string: ")
share_character = False

for first_character in first:
    for second_character in second:
        if first_character == second_character:
            share_character = True

print(share_character)


# Q107. Seating Plan
rows = int(input("Rows: "))
seats_per_row = int(input("Seats per row: "))

for row in range(1, rows + 1):
    print(f"Row {row}:", end=" ")

    for seat in range(1, seats_per_row + 1):
        print(seat, end=" ")

    print()


# Q108. Student Marks and Class Total
students = int(input("Number of students: "))
tests = int(input("Number of tests: "))
class_total = 0

for student in range(1, students + 1):
    student_total = 0

    for test in range(1, tests + 1):
        mark = int(input(f"Student {student}, test {test} mark: "))
        student_total += mark

    print(f"Student {student} total: {student_total}")
    class_total += student_total

print(f"Class total: {class_total}")


# Q109. Daily Rainfall Summary
days = int(input("Days: "))
stations = int(input("Stations: "))

for day in range(1, days + 1):
    daily_total = 0

    for station in range(1, stations + 1):
        rainfall = float(input(f"Day {day}, station {station}: "))
        daily_total += rainfall

    print(f"Day {day} total: {daily_total:g}")


# Q110. Largest of Several Numbers in Each Group
groups = int(input("Groups: "))
numbers_per_group = int(input("Numbers per group: "))

for group in range(1, groups + 1):
    largest = int(input(f"Group {group}, number 1: "))

    for position in range(2, numbers_per_group + 1):
        number = int(input(f"Group {group}, number {position}: "))

        if number > largest:
            largest = number

    print(largest)

# Q111. Sum of Numbers by Group and Position
group_1_first = int(input("Group 1, first number: "))
group_1_second = int(input("Group 1, second number: "))
group_1_third = int(input("Group 1, third number: "))

group_2_first = int(input("Group 2, first number: "))
group_2_second = int(input("Group 2, second number: "))
group_2_third = int(input("Group 2, third number: "))

print(
    "Group sums:",
    group_1_first + group_1_second + group_1_third,
    group_2_first + group_2_second + group_2_third
)

print(
    "Position sums:",
    group_1_first + group_2_first,
    group_1_second + group_2_second,
    group_1_third + group_2_third
)


# Q112. Number Pair Comparison Table
n = int(input("N: "))

for row in range(1, n + 1):
    for column in range(1, n + 1):
        print(row + column, end=" ")
    print()


# Q113. Count Zeroes in a Number Sequence
n = int(input("How many numbers? "))
zero_count = 0

for position in range(n):
    number = int(input("Number: "))

    if number == 0:
        zero_count += 1

print(zero_count)


# Q114. Print Row and Column Coordinates
rows = int(input("Rows: "))
columns = int(input("Columns: "))

for row in range(rows):
    for column in range(columns):
        print(f"({row}, {column})", end=" ")
    print()


# Q115. Find Every Occurrence of a Substring
text = input("Text: ")
pattern = input("Pattern: ")
found_match = False

for start in range(len(text) - len(pattern) + 1):
    matches = True

    for offset in range(len(pattern)):
        if text[start + offset] != pattern[offset]:
            matches = False
            break

    if matches:
        print(start, end=" ")
        found_match = True

if not found_match:
    print("No matches")


# Q116. Count Matching Character Pairs
text = input("String: ")
pair_count = 0

for first_position in range(len(text)):
    for second_position in range(first_position + 1, len(text)):
        if text[first_position] == text[second_position]:
            pair_count += 1

print(pair_count)


# Q117. Check Whether Two Strings Are Anagrams
first = input("First string: ")
second = input("Second string: ")
are_anagrams = len(first) == len(second)

for character in first:
    first_count = 0
    second_count = 0

    for item in first:
        if item == character:
            first_count += 1

    for item in second:
        if item == character:
            second_count += 1

    if first_count != second_count:
        are_anagrams = False

print(are_anagrams)


# Q118. Print Character Frequency Without a Dictionary
text = input("String: ")

for position in range(len(text)):
    appeared_before = False

    for earlier_position in range(position):
        if text[earlier_position] == text[position]:
            appeared_before = True

    if not appeared_before:
        frequency = 0

        for character in text:
            if character == text[position]:
                frequency += 1

        print(f"{text[position]}: {frequency}")


# Q119. Find Repeated Adjacent Characters
text = input("String: ")
position = 0

while position < len(text):
    end = position + 1

    while end < len(text) and text[end] == text[position]:
        end += 1

    run_length = end - position

    if run_length >= 2:
        print(f"{text[position]}: {run_length}")

    position = end


# Q120. Compare Two Words Position by Position
first = input("First word: ")
second = input("Second word: ")
different_positions = 0

for position in range(len(first)):
    if first[position] != second[position]:
        different_positions += 1

print(different_positions)


# Q121. Print All Pythagorean Triples up to N
n = int(input("N: "))

for c in range(1, n + 1):
    for b in range(1, c):
        for a in range(1, b):
            if a * a + b * b == c * c:
                print(a, b, c)


# Q122. Find Numbers Equal to the Sum of Their Proper Divisors
n = int(input("N: "))

for number in range(2, n + 1):
    proper_divisor_sum = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            proper_divisor_sum += divisor

    if proper_divisor_sum == number:
        print(number)


# Q123. Print Unique Products in Increasing Factor Order
n = int(input("N: "))

for first_factor in range(1, n + 1):
    for second_factor in range(first_factor, n + 1):
        product = first_factor * second_factor
        appeared_earlier = False

        for earlier_first in range(1, n + 1):
            for earlier_second in range(earlier_first, n + 1):
                if (earlier_first < first_factor or
                        (earlier_first == first_factor and
                         earlier_second < second_factor)):
                    if earlier_first * earlier_second == product:
                        appeared_earlier = True

        if not appeared_earlier:
            print(product, end=" ")


# Q124. Find All Pairs of Prime Numbers with a Given Sum
n = int(input("Even integer greater than 2: "))

for first_number in range(2, n // 2 + 1):
    second_number = n - first_number
    first_is_prime = True
    second_is_prime = True

    for divisor in range(2, first_number):
        if first_number % divisor == 0:
            first_is_prime = False
            break

    for divisor in range(2, second_number):
        if second_number % divisor == 0:
            second_is_prime = False
            break

    if first_is_prime and second_is_prime:
        print(first_number, second_number)


# Q125. Check a Magic-Sum Pattern
n = int(input("Enter an odd integer: "))

for row in range(1, n + 1):
    row_sum = 0

    for column in range(1, n + 1):
        value = row + column
        print(value, end=" ")
        row_sum += value

    print()

print("Row sums:", end=" ")

for row in range(1, n + 1):
    row_sum = 0

    for column in range(1, n + 1):
        row_sum += row + column

    print(row_sum, end=" ")


# Q126. Count Peaks in a Number Sequence
n = int(input("How many numbers? "))

if n < 3:
    print(0)
else:
    previous = int(input("Number: "))
    current = int(input("Number: "))
    peak_count = 0

    for position in range(2, n):
        following = int(input("Number: "))

        if current > previous and current > following:
            peak_count += 1

        previous = current
        current = following

    print(peak_count)


# Q127. Find Repeated Digit Sums
number = input("Positive integer: ")
has_repeated_pair_sum = False

for first_position in range(len(number)):
    for second_position in range(first_position + 1, len(number)):
        pair_sum = int(number[first_position]) + int(number[second_position])

        for other_first in range(len(number)):
            for other_second in range(other_first + 1, len(number)):
                different_pair = (
                    other_first != first_position or
                    other_second != second_position
                )

                other_sum = int(number[other_first]) + int(number[other_second])

                if different_pair and pair_sum == other_sum:
                    has_repeated_pair_sum = True

if has_repeated_pair_sum:
    print("Repeated pair sums exist")
else:
    print("No repeated pair sums")


# Q128. Number Pattern from Row and Column
n = int(input("N: "))

for row in range(1, n + 1):
    for column in range(1, n + 1):
        print(abs(row - column), end=" ")
    print()


# Q129. Compare Digits with Their Neighbours
number = input("Positive integer: ")
peak_count = 0

for position in range(1, len(number) - 1):
    if (number[position] > number[position - 1] and
            number[position] > number[position + 1]):
        peak_count += 1

print(peak_count)


# Q130. Count Increasing Digit Pairs
number = input("Positive integer: ")
pair_count = 0

for first_position in range(len(number)):
    for second_position in range(first_position + 1, len(number)):
        if number[first_position] < number[second_position]:
            pair_count += 1

print(pair_count)


# Q131. Character Frequency Compression Without a Dictionary
text = input("String: ")
result = ""

for position in range(len(text)):
    appeared_before = False

    for earlier_position in range(position):
        if text[earlier_position] == text[position]:
            appeared_before = True

    if not appeared_before:
        frequency = 0

        for character in text:
            if character == text[position]:
                frequency += 1

        result += text[position] + str(frequency)

print(result)