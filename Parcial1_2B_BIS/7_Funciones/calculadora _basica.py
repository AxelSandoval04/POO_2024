def solicitarDatos():
    print("\n")
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    return n1, n2

def getCalculadora(num1, num2, operacion):
    if operacion == 1 or operacion == "suma" or operacion == "+":
        result = num1 + num2
        print(f"Resultado: {result}")
    elif operacion == 2 or operacion == "resta" or operacion == "-":
        result = num1 - num2
        print(f"Resultado: {result}")
    elif operacion == 3 or operacion == "multiplicacion" or operacion == "*":
        result = num1 * num2
        print(f"Resultado: {result}")
    elif operacion == 4 or operacion == "division" or operacion == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Resultado: {result}")
        else:
            print("Error: División por cero no permitida")
    else:
        print("Operación no válida")


def main():
    while True:
        print("\nSeleccione la operación a realizar:")
        print("1. Suma. +")
        print("2. Resta. -")
        print("3. Multiplicación. *")
        print("4. División. /")
        print("5. Salir")
        
        operacion =(input("Operación: "))
        
        if operacion == 5:
            print("Saliendo...")
            break
        
        num1, num2 = solicitarDatos()
        getCalculadora(num1, num2, operacion)

if __name__ == "__main__":
    main()

