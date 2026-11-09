# Requirement 1: Create a list of courses taken at Walsh College, stored in all lowercase
courses_taken = ["it 408 database design", "it 301 systems analysis", "mgt 305 organizational behavior", "acc 201 financial accounting"]
courses_taken = [course.lower() for course in courses_taken]

# Requirement 2: Sort the list and print each element with the message, course in uppercase
courses_taken.sort()
for course in courses_taken:
    print(f"I have taken {course.upper()} at Walsh College.")

# Requirement 3: Add courses planned for next term, re-sort, and print with the message above the list
upcoming_courses = ["it 450 web development", "it 420 information security"]
all_courses = courses_taken + upcoming_courses
all_courses.sort()
print("\nThis is my course of study with upcoming courses added:")
for course in all_courses:
    print(course)

# Requirement 4: Remove courses already taken, printing each removed course after the message
print("\nI do not have to take these courses:")
for course in courses_taken:
    all_courses.remove(course)
    print(course)

# Requirement 5: Print the remaining courses, each on its own line, with the message above
print("\nI plan to take the following courses next term")
for course in all_courses:
    print(course)

# Requirement 6: Create a list of numbers from 1 to 1000 that are divisible by 6
numbers = [n for n in range(1, 1001) if n % 6 == 0]

# Requirement 7: Print the first 20 numbers, each on its own line, with the message above
print("\nHere are twenty numbers divisible by 6.")
for n in numbers[:20]:
    print(n)

# Requirement 8: Calculate the maximum number in the original large list and store it in a variable
max_number = max(numbers)

# Requirement 9: Print the maximum value with the message
print(f"\nThe maximum value in the list is: {max_number}")

# Requirement 10: Sum the values from the 10th through the 50th value (inclusive),
# store in a variable, and print with the message
# (10th value is index 9, 50th value is index 49, so the slice is [9:50])
sum_of_values = sum(numbers[9:50])
print(f"Here is the sum of several values in the list: {sum_of_values}")

# Requirement 11: Overwrite the variable that held the courses taken with the original large list of numbers
courses_taken = numbers