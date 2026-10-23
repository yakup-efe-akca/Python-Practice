with open("students.txt", "w") as file:
    file.write("Ali,85\n")
    file.write("Ayse,92\n")
    file.write("Mehmet,67\n")

with open("students.txt", "r") as file:
    for line in file:
        name, grade = line.strip().split(",")
        print(f"{name}: {grade}")

