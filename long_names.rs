names = ["Ana", "Benjamin", "Chloe"]
lengths = {n: len() for n in names}
print(lengths)
long_names = [n for n in names if len() > 3]
print(long_names)