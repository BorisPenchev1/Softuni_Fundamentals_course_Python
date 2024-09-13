n = int(input("Number of lines: "))
all_nums_lst = []
filtered_nums_lst = []

for i in range (n) :
    current_number = int(input())

    all_nums_lst.append(current_number)

command = input("Filter by: ")

if command == "even" :
    for i in range (len(all_nums_lst)) :
        if all_nums_lst[i] % 2 == 0 :
            filtered_nums_lst.append(all_nums_lst[i])
        else: 
            continue
    print(filtered_nums_lst)

if command == "odd" :
    for i in range (len(all_nums_lst)) :
        if all_nums_lst[i] % 2 != 0 :
            filtered_nums_lst.append(all_nums_lst[i])
        else:
            continue
    print(filtered_nums_lst)

if command == "negative" :
    for i in range (len(all_nums_lst)) :
        if all_nums_lst[i]  < 0 :
            filtered_nums_lst.append(all_nums_lst[i])
        else:
            continue
    print(filtered_nums_lst)

if command == "positive" :
    for i in range (len(all_nums_lst)) :
        if all_nums_lst[i] >= 0 :
            filtered_nums_lst.append(all_nums_lst[i])
        else:
            continue
    print(filtered_nums_lst)