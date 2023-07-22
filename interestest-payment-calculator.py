def cal(prestamo, interes, meses):
    total = prestamo * interes 
    cuotas = total / meses
    print(f"Tenés {meses} cuotas de ${cuotas} y el total es de ${total}")
    

def main():
    prestamo = int(input("Ingresa el monto el prestamo "))
    meses = int(input("Ingrese la cantidad de meses "))
    interes = 0
    
    if meses < 3 or meses == 3:
        interes = 1.1
        cal(prestamo, interes, meses)
    elif meses < 6 or meses == 6:
        interes = 1.3
        cal(prestamo, interes, meses)
    elif meses < 12 or meses == 12:
        interes = 1.6
        cal(prestamo, interes, meses)
    else:
        interes = 1.9
        cal(prestamo, interes, meses)
        
    
    
main()