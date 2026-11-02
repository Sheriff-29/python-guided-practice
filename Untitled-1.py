items = ["milk", "eggs", "bread"]

with open ("shopping.txt", "w", encoding="utf8") as f :
     for item in items
        f.write(item + "\n")

with open("shopping.txt", encoding="utf-8") as f:
     for i, line in enumerate(f, start=1):
            print(f"{i}. {line.strip()}")
 
