numbers = list(map(int, input("Numbers: ").split(", ")))
even_nums = [i for i in numbers if i % 2 == 0]
result = []

for i in even_nums :
    result.append(numbers.index(i))

print(result)
    