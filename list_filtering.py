nums = [-1, -2, 3, 4]

for n in nums:
    if n < 0:
        nums.remove(n)

print(nums)


nums = [-1, -2, 3, 4]

kept = []

for n in nums:
    if n >= 0:
        kept.append(n)

print(kept)


nums = [-1, -2, 3, 4]

for n in nums.copy():
    if n < 0:
        nums.remove(n)

print(nums)