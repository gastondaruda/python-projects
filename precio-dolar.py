import requests

url = 'https://api.bluelytics.com.ar/v2/latest'
response = requests.get(url)
dolar_blue = response.json()['blue']['value_avg']
euro_blue = response.json()['blue_euro']['value_avg']

def main():
    print("Converts divisas to Pesos")
    
    moneda = input("Qué moneda desea comprar? (Euro/Dolar) ").lower()
    
    if moneda == "euro":
        cantidad = int(input("Ingrese la cantidad"))
        resultado = cantidad * euro_blue
        print(f"El {moneda} es {euro_blue}, el total es de ${resultado}")
    elif moneda == "dolar":
        cantidad = int(input("Ingrese la cantidad"))
        resultado = cantidad * dolar_blue
        print(f"El {moneda} es {dolar_blue}, total es de ${resultado}")
    else:
        print("Ingrese una moneda válida por favor")


main()
