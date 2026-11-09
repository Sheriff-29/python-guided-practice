names = ["Ana", "Ben", "Chloe", "Dan"]
grades = [14.5, 8.0, 17.0, 11.5]

total = 0
count = 0

for name, grade in zip(names, grades):

    count = count + 1
    total = total + grade

    if grade >= 10:
        result = "PASS"
    else:
        result = "FAIL"

    print(f"{count}. {name}: {grade} {result}")

average = total / count

print(f"Average: {average:.2f}")