# Not finished
#TODO: fix

words = input("Words: ").split(' ')
palindrome = input("Search Palindrome: ")
palindromes = []
times_found = 0
curr_word = ""


def Word(curr_word, times_found, words):

    for i in range(0, len(words)) :

        curr_word = words[i]

        if curr_word == palindrome:
            times_found += 1
        palindromes.append(curr_word)

    if curr_word == curr_word[::-1]:
        return curr_word


Word(curr_word, times_found, words)

print(palindromes)
print(f"Palindrome found {times_found} times.")

# Not finished
#TODO: fix