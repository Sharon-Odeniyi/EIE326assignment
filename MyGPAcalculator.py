# Simple GPA Calculator for 6 Courses

# Function to convert grade to grade point
def grade_to_point(grade):
    grade = grade.upper()
    if grade == 'A':
        return 5
    elif grade == 'B':
        return 4
    elif grade == 'C':
        return 3
    elif grade == 'D':
        return 2
    elif grade == 'E':
        return 1
    else:
        return 0  # For F or invalid grades

# Start GPA calculation
print("📘 GPA Calculator for 6 Courses")

total_points = 0
total_units = 0

# Repeat for 6 courses
for i in range(1, 7):
    print(f"\nCourse {i}:")
    course_code = input("Enter course code (e.g., MTH101): ")
    unit = int(input("Enter course unit: "))
    grade = input("Enter grade (A-F): ")

    point = grade_to_point(grade)
    total_points += point * unit
    total_units += unit

# Calculate GPA
if total_units > 0:
    gpa = total_points / total_units
    print(f"\n🎓 Your GPA is: {round(gpa, 2)}")
else:
    print("⚠️ No valid course units entered.")
