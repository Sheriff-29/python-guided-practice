d = {"Ana": 15, "Ben": 12}
print(d.get("Zoe", 0))


s = set()
print(s)


nums = [4, 2, 8, 1]
nums.sort()
print(nums)


with open("names.txt", "w", encoding="utf-8") as f:
    f.write("Meer\n")
    f.write("Ana\n")


with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New entry\n")


line = "Meer,21\n"
parts = line.strip().split(",")
print(parts)
print(repr(line))