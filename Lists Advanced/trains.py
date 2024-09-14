lenght = int(input("Number of wagons: "))
wagons = [0] * lenght
command =  ""   

while True :

    command = input()

    if command == "End" :
        break

    current_cmd = command.split(" ")

    if current_cmd[0] == "add" :
        wagons[-1] +=  int(current_cmd[1])
    elif current_cmd[0] == "insert" :
        wagons[int(current_cmd[1])] += int(current_cmd[2])
    elif current_cmd[0] == "leave" :
        wagons[int(current_cmd[1])] -= int(current_cmd[2])

print(wagons)
