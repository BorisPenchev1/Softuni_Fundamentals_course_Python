n = int(input("Enter an integer n: "))

for i in range(1, n + 1):
    
    digit_sum = sum(int(digit) for digit in str(i))
    
    is_special = digit_sum in [5, 7, 11]
    
    print(f"{i} -> {is_special}")
