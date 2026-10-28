items = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = {}

for item in items:
    if item not in counts:
        counts[item] = 0
    counts[item] += 1

print(counts)