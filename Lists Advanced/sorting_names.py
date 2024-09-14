names = input().split(', ')

sorted_names = sorted(names, key = lambda names: (-len(names), names))

print(sorted_names)