students = {
    "Ali": [80, 90, 70],
    "Ayse": [95, 85, 100],
    "Mehmet": [60, 45, 70],
    "Zeynep": [100, 90, 95]
}

def calculate_average(grades):
    total = 0
    number_of_grades = len(grades)
    for grade in grades:
        total += grade
    average = total / number_of_grades
    
    return average

def get_status(average):
    return "Passed" if average >= 70 else "Failed"

for name, notes in students.items():
    average = calculate_average(notes)
    print(f"{name}: {average:.2f} - {get_status(average)}")