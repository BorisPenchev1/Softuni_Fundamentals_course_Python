n = int(input())
positive_nums_lst = []
negative_nums_lst = []

for i in range (n) :
    curent_number = int(input())
    if curent_number >= 0 :
        positive_nums_lst.append(curent_number)
    else:
        negative_nums_lst.append(curent_number)

count_positives = len(positive_nums_lst)
sum_of_negatives = sum(negative_nums_lst)

print(positive_nums_lst)
print(negative_nums_lst)

print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")