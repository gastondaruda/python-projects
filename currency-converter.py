def main():
    print("Converts divisas to Pesos")
    
    moneda = input("Qué moneda desea comprar? (Euro/Dolar) ").lower()
    
    if moneda == "euro":
        cantidad = int(input("Ingrese la cantidad"))
        resultado = cantidad * 633
        print(f"El total es de ${resultado}")
    elif moneda == "dolar":
        cantidad = int(input("Ingrese la cantidad"))
        resultado = cantidad * 525
        print(f"El total es de ${resultado}")
    else:
        print("Ingrese una moneda válida por favor")
        #main()
        
        
main()