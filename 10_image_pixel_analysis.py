pixels = [
    [120, 200, 50],
    [255, 80, 190],
    [30, 160, 240]
]

def analyze_image(pixels):
    darkest = pixels[0][0]
    brightest = pixels[0][0]
    above_150 = 0
    total = 0
    count = 0

    for row in pixels:
        for col in row:
            total += col
            count += 1

            if col > brightest:
                brightest = col

            if col < darkest:
                darkest = col

            if col > 150:
                above_150 += 1

    average = total / count

    return brightest, darkest, average, above_150


brightest, darkest, average, above_150 = analyze_image(pixels)

print(f"Brightest pixel: {brightest}")
print(f"Darkest pixel: {darkest}")
print(f"Average brightness: {average:.2f}")
print(f"Pixels above 150: {above_150}")