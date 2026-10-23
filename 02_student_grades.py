grades = {
    "Ali": 85,
    "Ayse": 92,
    "Mehmet": 67,
    "Zeynep": 48,
    "Can": 75
}

passed_students = []
total = 0
max_grade = 0
best_student = ""
average = 0

for name, grade in grades.items():
    if grade >= 70:
        passed_students.append(name)
    if grade > max_grade:
            max_grade = grade
            best_student = name
    total += grade
        
average = total / len(grades)

print(f"Average: {average}")
print(f"Passed students: {passed_students}")
print(f"Highest grade: {best_student} ({max_grade})")