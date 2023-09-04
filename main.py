from calc import add, sub, mult, div


def calc():
    firstNumber = int(input("enter first Number !! "))
    operation = input("enter the operation !! ")
    secondNumber = int(input("enter second Number !! "))

    if operation == "add" :
        result = add(firstNumber, secondNumber)
    elif operation == "sub" :
        result = sub(firstNumber, secondNumber)

    elif operation == "mult" :
        result = mult(firstNumber, secondNumber)

    elif operation == "div" :
        result = div(firstNumber, secondNumber)

    else:
        result = "wrong operation"

    print(result)

    anotherOperation = input("Another Operation : yes or No ? ")
    if anotherOperation == "yes" or anotherOperation == "YES" :
        calc()
    else:
        exit()
    
    

    

calc()





