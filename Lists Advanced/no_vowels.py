word = str(input("Your word: "))
word_list = []
vowels = ['o','a'',u','e','i','I', 'E', 'U', 'A', 'O']

for i in word :
    word_list.append(i)

result = [i for i in word_list if i not in vowels]

print(''.join(result))