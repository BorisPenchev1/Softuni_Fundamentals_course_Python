input_order = []
correct_order = ["head", "body", "tail"]

part_of_body_1 = input()
input_order.append(part_of_body_1)
part_of_body_2 = input()
input_order.append(part_of_body_2)
part_of_body_3 = input()
input_order.append(part_of_body_3)

if input_order == correct_order :
    print("You wrote them in correct order !")

part_of_body_1 = correct_order[0]
input_order[0] = part_of_body_1
part_of_body_2 = correct_order[1]
input_order[1] = part_of_body_2
part_of_body_3 = correct_order[2]
input_order[2] = part_of_body_3

print(input_order)









