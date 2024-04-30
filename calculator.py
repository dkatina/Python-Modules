from operations import add, sub, multiply, divide, get_num




def calculator():
    x = get_num()
    while True:
        operation = input('+ | - | * | / | CE | X: ')
        if operation == 'CE':
            x = 0
            print(x)
            continue
        if operation == '+':
            y = get_num()
            x = add(x,y)
            print(x)
        elif operation =='-':
            y = get_num()
            x = sub(x,y)
            print(x)
        elif operation == '*':
            y = get_num()
            x = multiply(x,y)
            print(x)
        elif operation == '/':
            y = get_num()
            x = divide(x,y)
            print(x)
       
        elif operation == 'X':
            print('Goodbye')
            break
        else:
            print('Invalid option')

calculator()