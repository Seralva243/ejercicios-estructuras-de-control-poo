def diecisiete():
    suma = 0

    for i in range (1,101):
        suma += i**2
    
    print("La suma de los cuadrados de los 100 primeros numeros naturales es:", suma)

def dieciocho():

    n = int(input("ingrese un numero entero: "))
    suma = 0
    for i in range(n + 1, n + 101):
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
    elif n2 > n1:
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
    diecisiete()
    dieciocho()
    diecinueve()
    veinte()
    veintiuno()
    veintidos()
    veintitres()
    veintiseis()
    veintisiete()
    treinta()
if __name__ == "__main__":
    main()
