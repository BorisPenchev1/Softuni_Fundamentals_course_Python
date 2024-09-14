import sys

operator = ""
number_1 = 0
number_2 = 0

def calculator(operator, number_1, number_2):
    match operator :
        case "add":
            result = number_1 + number_2
            return result
        case "+":
            result = number_1 + number_2
            return result
        case "subtract":
            result = number_1 - number_2
            return result
        case "-":
            result = number_1 - number_2
            return result
        case "divide":
            result = number_1 / number_2
            return result
        case "/":
            result = number_1 / number_2
            return result
        case "multiply":
            result = number_1 * number_2
            return result
        case "*":
            result = number_1 * number_2
            return result
        case "exit":
            sys.exit(0)
        case "":
            print("Invalid operator")
            sys.exit(0)


while operator != "exit":
    operator = str(input("Operator or exit: "))
    calculator(operator, number_1, number_2)
    number_1 = int(input("First number: "))
    number_2 = int(input("Second number: "))
    print(calculator(operator, number_1, number_2))
    operator = ""


