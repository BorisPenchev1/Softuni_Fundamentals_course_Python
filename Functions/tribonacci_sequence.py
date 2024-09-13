number_of_length = int(input("Number of the length of your sequence: "))
tribonacci_sequence = [1, 1, 1]  # Initialize the sequence with three 1s

def Tribonacci_sequence(number_of_length, tribonacci_sequence):
    for i in range(3, number_of_length):  # Start from index 3
        next_value = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3]
        tribonacci_sequence.append(next_value)
    return tribonacci_sequence[:number_of_length]  # Slice in case the input length is less than 3

result = Tribonacci_sequence(number_of_length, tribonacci_sequence)
print(result)







