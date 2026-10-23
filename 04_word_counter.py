text = "Python is easy and Python is powerful"
words = text.lower().split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

max_count = 0
most_frequent = ""

for word, count in word_counts.items():
    if count > max_count:
        max_count = count
        most_frequent = word

print(f"Word counts: {word_counts}")
print(f"Most frequent: {most_frequent} ({max_count})")