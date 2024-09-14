food = float(input())
hay = float(input())
cover = float(input())
guinea_weight = float(input())


for i in range (1, 30 + 1) :
    food -= 0.300
    guinea_weight += 0.300

    if i % 2 == 0 :
        hay -= 5 / 100 * food
        
    if i % 3 == 0 :
        cover -= guinea_weight / 3

    if food <= 0 or hay <= 0 or cover <= 0 :
        print(f"Merry must go to the pet store!Food: {food:.2f}, Hay: {hay:.2f},Cover: {cover:.2f}.")
        break

if food >= 0 and hay >= 0 and cover >= 0 :
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f},Cover: {cover:.2f}.")