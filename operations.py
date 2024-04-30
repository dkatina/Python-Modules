


#add 2 nums
def add(x,y):
    return x+y

#subtract 2 nums
def sub(x,y):
    return x-y

#multiply 2nums
def multiply(x,y):
    return(x*y)


#divide (catching 0 division error) 2nums 

#try: lets us try code that could break
#except: lets us handle if it does break

def divide(x,y):
    try:
        quotient = x/y
    except ZeroDivisionError:
        print('No no no! Cant divide by zero')
        return x
    else:
        return quotient
    

def get_num():
    while True:
        try:
            x = int(input('>'))
        except:
            print('Please enter a number')
        else:
            return x
    
