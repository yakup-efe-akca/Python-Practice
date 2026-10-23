def calculate_total(*args):
    total = 0
    for item in args:
        total += item
    return total

def print_student(**kwargs):
    for first, second in kwargs.items():
            print(f"{first}: {second}")

print(calculate_total(10,20,30))
print_student(name="Ali", age=20, department="Computer Engineering")
    