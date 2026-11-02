def find_max(values):
    """Return the biggest value in a list."""
    best = values[0]
    for v in values:
        if v > best:
            best = v
    return best


def count_occurrences(items, target):
    """Count how many times target appears."""
    n = 0
    for x in items:
        if x == target:
            n += 1
    return n


def filter_by_value(d, minimum):
    """Return items with values above the minimum."""
    result = {}
    for k, v in d.items():
        if v >= minimum:
            result[k] = v
    return result


print(find_max([4, 9, 2]))
print(count_occurrences(["a", "b", "a"], "a"))
print(filter_by_value({"Ana": 15, "Ben": 9}, 10))