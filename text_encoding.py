with open("c.txt", "w", encoding="utf-8") as f:
    f.write("Chloé, Noël")

with open("c.txt", encoding="latin-1") as f:
    print(f.read())


with open("c.txt", "w", encoding="utf-8") as f:
    f.write("Chloé, Noël")

with open("c.txt", encoding="utf-8") as f:
    print(f.read())