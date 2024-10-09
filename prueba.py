# Programa en Python

def main():
    valor = potencia()
    print(f"El valor de su operación es: {valor}")


def potencia():
    a = eval(input("Hola, ingrese el primer valor: "))
    b = eval(input("Hola, ingrese el segundo valor: "))    

    return a**b

main()