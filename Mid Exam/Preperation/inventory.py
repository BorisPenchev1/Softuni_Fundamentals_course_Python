inventory = input().split(", ")
command = ""

while command != "Craft!":
    command = input().split(" - ")

    match command[0]:
        case "Collect":
            if command[1] not in inventory:
                inventory.append(command[1])
        case "Drop":
            if command[1] in inventory:
                inventory.remove(command[1])
        case "Combine Items":
            combine_comm = command[1].split(":")
            if combine_comm[0] in inventory:
                insert_index = inventory.index(combine_comm[0]) 
                inventory.insert(insert_index + 1, combine_comm[1])  
        case "Renew":
            if command[1] in inventory:
                inventory.remove(command[1])
                inventory.append(command[1])
        case "Craft!":
            break

print(", ".join(inventory))
