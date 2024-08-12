orders = int(input("Number of orders: "))
ready_orders = 0
total_price_list = []

for i in range(1, orders + 1):
    print(f"Order {i}")
    
    price_per_one = float(input("Price per capsule: "))
    if price_per_one <= 0.00 or price_per_one > 100.00:
        print("Invalid price. Go to next order.")
        continue

    days = int(input("Days: "))
    if days < 1 or days > 31:
        print("Invalid number of days. Go to next order.")
        continue

    capsules_per_day = int(input("Capsules per day: "))
    if capsules_per_day < 1 or capsules_per_day > 2000:
        print("Invalid number of capsules. Go to next order.")
        continue

    price = price_per_one * capsules_per_day * days
    total_price_list.append(price)
    ready_orders += 1

    print(f"The price of the order is: {price:.2f}")

total_price = sum(total_price_list)
print(f"The total price is: {total_price:.2f}")
