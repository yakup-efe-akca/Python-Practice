numbers = [3, 8, 12, 5, 20, 7, 16, 9]

new_list = [number**2 for number in numbers if number % 2 == 0]

print(f"{new_list}")