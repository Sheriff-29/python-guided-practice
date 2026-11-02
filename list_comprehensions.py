prices = [12.5, 8.0, 30.0]

with_tax = []
for p in prices:
    with_tax.append(round(p * 1.2, 2))

print(with_tax)


prices = [12.5, 8.0, 30.0]
with_tax = [round(p * 1.2, 2) for p in prices]

print(with_tax)


lines = ["the cat sat", "a big dog ran"]

words = []
for line in lines:
    for w in line.split():
        if len(w) > 2 and w != "the":
            words.append(w.upper())

print(words)


lines = ["the cat sat", "a big dog ran"]
words = [w.upper() for line in lines
         for w in line.split()
         if len(w) > 2 and w != "the"]

print(words)