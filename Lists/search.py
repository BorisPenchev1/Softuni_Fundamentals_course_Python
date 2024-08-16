n = int(input("Number of sentences: "))
keyword = input("Your keyword: ")

all_strings_lst = []
keyword_lst = []

for i in range (n):
    current_string = str(input(f"Sentence {i + 1}: "))

    all_strings_lst.append(current_string)

    if keyword in current_string : 
        keyword_lst.append(current_string)

print(all_strings_lst)
print(keyword_lst)