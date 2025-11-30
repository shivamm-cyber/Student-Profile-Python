# Name: 
# Roll No: 
# Course: BCA
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-1 Mini Project
# Title: Student Profile Console App
# Date: 

# ----------------------------------------
# Welcome Message
# ----------------------------------------
print("========================================")
print("     Welcome to Student Profile System  ")
print("========================================")
print("This console app will create your student profile,")
print("demonstrate Python operators, and show string formatting.\n")

# ----------------------------------------
# Task 2: Input & Variables
# ----------------------------------------
student_name = input("Enter your full name: ")
roll_number = input("Enter your roll number: ")
program = input("Enter your program (e.g., BCA): ")
university = input("Enter your university name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

print("\nProfile data collected successfully!\n")

# ----------------------------------------
# Task 3: Operators Demonstration
# ----------------------------------------
print("----- Python Operators Demonstration -----")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic Operators
print("\nArithmetic Operators:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} // {num2} = {num1 // num2}")

# Assignment Operators
print("\nAssignment Operators:")
x = num1
x += num2
print(f"x += num2 → {x}")
x -= num2
print(f"x -= num2 → {x}")
x *= num2
print(f"x *= num2 → {x}")
x /= num2
print(f"x /= num2 → {x}")

# Comparison Operators
print("\nComparison Operators:")
print(f"{num1} > {num2} → {num1 > num2}")
print(f"{num1} < {num2} → {num1 < num2}")
print(f"{num1} == {num2} → {num1 == num2}")
print(f"{num1} != {num2} → {num1 != num2}")

# Logical Operators
print("\nLogical Operators:")
print(f"({num1} > 0 and {num2} > 0) → {num1 > 0 and num2 > 0}")
print(f"({num1} > 0 or {num2} > 0) → {num1 > 0 or num2 > 0}")
print(f"not({num1} > {num2}) → {not(num1 > num2)}")

# Identity Operators
print("\nIdentity Operators:")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(f"a is b → {a is b}")
print(f"a is not c → {a is not c}")

# Membership Operators
print("\nMembership Operators:")
sample_text = "Python Programming"
print(f"'P' in sample_text → {'P' in sample_text}")
print(f"'z' not in sample_text → {'z' not in sample_text}")

# ----------------------------------------
# Task 4: Strings & Formatting
# ----------------------------------------
print("\n----- String Operations & Formatting -----")

# String concatenation
greeting = "Hello, " + student_name + "!"
print(greeting)

# f-strings
intro = f"My name is {student_name}, and I study {program} at {university}."
print(intro)

# Escape characters
print("Using escape characters:\n\tName: \"{}\"\n\tHobby: \"{}\"".format(student_name, hobby))

# String methods
print("\nString Methods Demonstration:")
print(f"Uppercase: {student_name.upper()}")
print(f"Lowercase: {student_name.lower()}")
print(f"Title Case: {student_name.title()}")
print(f"Replace spaces with underscores: {student_name.replace(' ', '_')}")
print(f"Count of 'a' in your name: {student_name.lower().count('a')}")

# ----------------------------------------
# Task 5: Final Output — Student Profile Card
# ----------------------------------------
print("\n----------------------------------------")
print("        STUDENT PROFILE SYSTEM          ")
print("----------------------------------------")
print(f"Name:            {student_name}")
print(f"Roll No:         {roll_number}")
print(f"Course:          {program}")
print(f"University:      {university}")
print(f"City:            {city}")
print(f"Age:             {age}")
print(f"Hobby:           {hobby}")
print("----------------------------------------")
print("Welcome to Python Programming !")
print("----------------------------------------\n")

# ----------------------------------------
# Task 6: Bonus Task — Save to File
# ----------------------------------------
save_choice = input("Do you want to save your profile? (yes/no): ").lower()
if save_choice == "yes":
    with open("student_profile.txt", "w") as file:
        file.write("----------------------------------------\n")
        file.write("        STUDENT PROFILE SYSTEM          \n")
        file.write("----------------------------------------\n")
        file.write(f"Name:            {student_name}\n")
        file.write(f"Roll No:         {roll_number}\n")
        file.write(f"Course:          {program}\n")
        file.write(f"University:      {university}\n")
        file.write(f"City:            {city}\n")
        file.write(f"Age:             {age}\n")
        file.write(f"Hobby:           {hobby}\n")
        file.write("----------------------------------------\n")
        file.write("Welcome to Python Programming !\n")
    print("\nProfile saved successfully to 'student_profile.txt'.")
else:
    print("\nProfile not saved. Thank you for using the app!")
