# n = int(input())

# for i in range (1, n + 1):
#     num = int(input())
#     if num % 2 != 0 :
#         print(f"{num} is odd")
#         break
# else:
#     print("All numbers are even")

# Na gospodina
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

n = int(input())

for i in range (1, n + 1):
    num = int(input())
    if num % 2 == 0 :
        continue
    else:
        print(f"{num} is odd")

if i == n :
    print("All numbers are even.")

    


