numbers = [12, 7, 25, 8, 14, 3, 20, 11]

even_numbers = []
total = 0
average = 0

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

for even in even_numbers:
    total += even

average = total / len(even_numbers)

print(f"Even numbers: {even_numbers}")
print(f"Sum: {total}")
print(f"Average: {average}")