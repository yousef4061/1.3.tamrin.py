import math

print("welcome to my calculator")
while True:
    print("+ : sum")
    print("- : sub")
    print("* : mul")
    print("/ : div")
    print("sin")
    print("log")
    print("** now operations **")
    print("^ : power")
    print("sqrt : square root")
    print("cos : cosine")
    print("tan : tangent")
    print("exit")
    print("please enter your choice: ")
    op = input()

    if op == "exit":
          print("thank you for using my app")
          print("good bye")
          break

    if op == "+" or op =="-" or op =="*" or op =="/" or op =="^":
        a = float(input("enter first number: "))    #عداد اعشاری  و پایینیش 
        b = float(input("enter second number: "))
    else:
        a = float(input("enter first number: "))
        
    if op == "+":
        result = a + b 

    elif op == "-":
        result = a - b

    elif op == "*":
        result = a * b

    elif op == "/":
        if b == 0:
            print ("error: cannot divide by zero")
            continue
        else:
            result = a / b
    elif op == "^":
        result = a ** b
    elif op == "sqrt":
        if a <= 0:
            print("error: logarithm must be greater than zero1")
            continue
        else:
            result = math.sqrt(a)   
    elif op == "sin":
        result = math.sin(a)
    elif op == "cos":
        result = math.cos(a)
    elif op == "tan":
        result = math.tan(a)
    elif op == "log":
        result = math.log(a)
        if a <= 0:
            print("error: logarithm must be greater than zero!")
            continue
        else:
            result = math.log(a)
    else:
        print("invalid operation! please try again.")
        continue
    print(result)

#کامل شد