def uno():

    print("Hola, ya se imprimir frases")

def dos():

    print(273)
    print(597)

def tres():

    print(3.1)
    print(2.7)

def cuatro():

    suma = 1234 + 532
    print("La suma de 1234 y 532 es:", suma)

def cinco():

    resta = 1234 - 532
    print("La resta de 1234 y 532 es:", resta)

def seis():

    multiplicacion = 1234 * 532
    print("La multiplicación de 1234 y 532 es:", multiplicacion)

def siete():

    division = 1234 / 532
    print("La division de 1234 entre 532 es:", division)

def ocho():

    for i in range (1,4):
        print(i)

def nueve():

    for i in range (1,10):
        print(i)    

def diez():

    for i in range (1,10001):
        print(i)

def once():

    for i in range (5,11):
        print(i)    

def doce():

    for i in range (5,16):
        print(i)

def trece():

    for i in range (5,15001):
        print(i)

def catorce():

    for i in range (200):
        print("hola")

def quince():

    for i in range (1,31):
        print(f"El cuadrado de {i} es {i**2}")

def dieciseis():

    for i in range (1,21):
        producto *= i
        print("La multiplicacion de los 20 primeros numeros naturales es:", producto)

def diecisiete():
    suma = 0

    for i in range (1,101):
        suma += i**2
    
    print("La suma de los cuadrados de los 100 primeros numeros naturales es:", suma)

def dieciocho():

    n = int(input("ingrese un numero entero: "))
    suma = 0
    for i in range (n + 1, n + 101):
        suma += i
        print(f"La suma de los 100 numeros siguientes a {n} es: {suma}")

def diecinueve():

    tasa_cambio = 1.1 
    euros = float(input("Ingrese la cantidad en euros: "))
    dolares = euros * tasa_cambio

    print(f"{euros:.2f} € equivalen a {dolares:.2f} $")

def veinte():

    altura = float(input("Ingrese la altura del rectangulo: "))
    anchura = float(input("Ingrese la anchura dedl rectangulo: "))
    area = altura * anchura
    print("El area del rectangulo es:", area)

def veintiuno():

    n1 = float(input("Ingrese el priimer numero: "))
    n2 = float(input("Ingrese el segundo numero: "))

    if n1 > n2:
        print(f"El mayor es {n1} y el menor es {n2}")
    elif n2 < n1:
        print(f"El mayor es {n2} y el menor es {n1}")
    else:
        print("Ambos numeros son iguales")

def veintidos():

    n = int(input("Ingrese un numero entero: "))
    print(f"Los numeros impares menores que {n} son:")
    
    for i in range (1, n, 2):
        print(i)

def veintitres():

    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))

    while b != 0:
        a, b = b, a % b
    print("El maximo comun divisor es:", a)

def veinticuatro():

    import math
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))
    
    if a == 0:
        print("No es una ecuacion cuadratica")
    else:
        D = b**2 - 4*a*c
    if D < 0:
        print("La ecuacion no tiene soluciones reales.")
    elif D == 0:
        x = -b / (2*a)
        print("La ecuacion tiene una unica solucion real:", x)
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("La ecuacion tiene dos soluciones reales:")
        print("x1 =", x1)
        print("x2 =", x2)

def factorial(n):

    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)  
    
def ejecutar_factorial():

    n = int(input("Ingrese un número entero: "))
    print("El factorial de", n, "es:", factorial(n))

def ackermann(m, n):

    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
    
def ejecutar_ackermann():

    m = int(input("Ingrese m: "))
    n = int(input("Ingrese n: "))

    print(f"Ackermann({m}, {n}) =", ackermann(m, n))

def veintiseis():

    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = int(input("Ingrese el tercer numero: "))

    menor = min(a,b,c)
    mayor = max(a,b,c)
    
    print("El numero menor es:", menor)
    print("El numero mayor es:", mayor)

def veintisiete():

    while True:
        f = float(input("Ingrese una temperatura en °F (999 para salir): "))

        if f == 999:
            print("programa finalizado.")
            break

        c = (f - 32) * 5 / 9
        print(f"{f}°F equivalen a {c:.2f} °C")

def veintiocho():
    for i in range (1,5):
        match i:
            case 1:
                print("Caso 1: Hola")
            case 2:
                print("Caso 2: Como estas")
            case 3:
                print("Caso 3: Adios")
            case _:
                print("Caso por defecto: ninguna coincidencia")

def treinta():
    for num in range (2, 51):
        es_primo = True
        for divisor in range(2, num):
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            print(num)
        




def main():
    uno()
    dos()
    tres()
    cuatro()
    cinco()
    seis()     
    siete()
    ocho()
    nueve()
    diez()
    once()
    doce()
    trece()
    catorce()
    quince()
    dieciseis()
    diecisiete()
    dieciocho()
    diecinueve()
    veinte()
    veintiuno()
    veintidos()
    veintitres()
    veinticuatro()
    ejecutar_factorial()
    ejecutar_ackermann()
    veintiseis()
    veintisiete()
    veintiocho()
    treinta()
    pass
if __name__ == "__main__":
    main()
