# NOT FINSHED

main_sequence = list(map(int, input().split(' ')))
current_sequence = []
message = ""
sentence = str(input())
sentence_len = len(sentence)
difference = 0 


for i in main_sequence :

    if main_sequence[i] != " " :    
        
        sum_current_sequence = sum(current_sequence)

        if sum_current_sequence > sentence_len :
            difference = sum_current_sequence - sentence_len

            message.__add__(sentence[difference])
            sentence.replace(sentence[difference], "")
        else:
            message.__add__(sentence[sum_current_sequence])
            sentence.replace(sentence[difference], "")
    else:
        current_sequence.append(main_sequence[int(i)])

    main_sequence.replace(str(current_sequence), "")
    

print(message)

            


# NOT FINISHED



    
