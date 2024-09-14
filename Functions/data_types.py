data_type = input("Data type: ")
num = input("Number: ")

def Data_type_func(data_type, num):
    
    match data_type :
        case "int" :
            print (int(num) * 2)
        case "string" :
            print(f"${num}$") 
        case "real" :
            print(f"{int(num) * 1.5:.2f}") 

Data_type_func(data_type, num)