#functions
def multiply(a, b):
    multanswer = int(a * b)
    print(multanswer)
    return multanswer

def add(a, b):
    addanswer = int(a + b)
    print(addanswer)
    return addanswer
    
def divide(a, b):
    divideanswer = int(a // b)
    print(divideanswer)
    return divideanswer

def divide2(a, b):
    answer = int(a / b)
    print(answer)
    return answer

def subtract(a, b):
    subtractanswer = int(a - b)
    print(subtractanswer)
    return subtractanswer

def remainder(a, b):
    remainderanswer = int(a % b)
    return remainderanswer

#code 
a = int(input("input a number: "))
x = 1
while x == 1:
    compute = input("do you want to multiply, add, divide, or subtract: ")
    print(compute, "by what? ")
    b = int(input())
    if compute == "multiply": #multiplication step 
        multanswer = multiply(a, b)
        '''
        should multiply a and b and assign it to multanswer, 
        and then it should print the multanswer in the function.
        under the if statement it should execute the function, 
        and then make multanswer the multiply.
        '''
        yesno = input("anything else? yes or no: ")
        if yesno == "yes": 
            x = x - 1
            x = x + 1
            a = multanswer
        else: 
            x - 1
            x + 1
            print("Your answer is:", multanswer)
            a = int(input("input a number: "))
    elif compute == "add": #adding steps
        add(a, b)
        addanswer = add(a, b)
        yesno = input("anything else? yes or no: ")
        if yesno == "yes": 
            x = x - 1
            x = x + 1
            a = addanswer
        else: 
            x - 1
            x + 1
            print(addanswer)
            a = int(input("input a number: "))
    elif compute == "divide": #dividing steps
        if a < b:
            divide2(a, b)
            answer = divide2(a, b)
        else:
            divide(a, b)
            divideanswer = divide(a, b)
        remainder(a, b)
        remainderanswer = remainder(a, b)
        yesno = input("anything else? yes or no: ")
        if yesno == "yes": 
            print("do you want the remainder?")
            yesno2 = input("yes or no? ")
            if yesno2 == "yes":
                print(remainderanswer)
            x = x - 1
            x = x + 1
            a = divideanswer
        else: 
            x - 1
            x + 1
            print(divideanswer)
            a = int(input("input a number: "))
    elif compute == "subtract": #subtracting steps
        subtract(a, b)
        subtractanswer = subtract(a, b)
        yesno = input("anything else? yes or no: ")
        if yesno == "yes": 
            x = x - 1
            x = x + 1
            a = subtractanswer
        else: 
            x - 1
            x + 1
            print(subtractanswer)
            a = int(input("input a number: "))
    elif compute == "done" or "no":
        x -= 1
        x += 1
        a = int(input("input a number: "))
