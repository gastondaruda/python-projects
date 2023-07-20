def add(a,b):
    answer = a + b
    print(f"{a} + {b} = {answer}")
    return f"{a} + {b} = {answer}"

def rest(a,b):
    answer = a - b
    print(f"{a} - {b} = {answer}")
    return f"{a} - {b} = {answer}"

def divide(a,b):
    answer = a - b
    print(f"{a} / {b} = {answer}")
    return f"{a} / {b} = {answer}"

def multiply(a,b):
    answer = a * b
    print(f"{a} * {b} = {answer}")
    return f"{a} * {b} = {answer}"

def calculate():
    a = int(input("Ingrese el primer valor"))
    operation = input("¿Qué operación desea hacer?")
    b = int(input("Ingrese el segundo valor"))
    
    if operation == "+":
        add(a,b)
    elif operation == "-":
        rest(a,b)
    elif operation == "/":
        divide(a,b)
    elif operation == "*":
        multiply(a,b)
    else:
        print("Hubo un error")
        
        
calculate()