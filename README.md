# autor: Sergio Alejandro Vazquez Pineda
# ejercicios-estructuras-de-control-poo


# def diecisiete(): 
# primero inicializamos la suma, luego ponemos el rango del 1 al 100, luego le damos el valor a la suma de la suma de i**2
# i**2 significa elevado al 2, luego imprimimos el texto y el resultado.

suma = 0     

for i in range (1,101): 
suma += i**2 
print("La suma de los cuadrados de los 100 primeros numeros naturales es:", suma)

La suma de los cuadrados de los 100 primeros numeros naturales es: 338350 

# def dieciocho():
# primero pedimos que ingrese el numero, luego inicializamos la suma, ponemos el rango desde el numero siguiente hasta los 100 siguientes 
# luego le damos el valor a la suma de la suma de cada numero que sigue hasta los 100 siguientes y lluego imprimmiimos el resultado 

    n = int(input("ingrese un numero entero: "))
    suma = 0
    for i in range(n + 1, n + 101):
        suma += i
    print(f"La suma de los 100 numeros siguientes a {n} es: {suma}")

ingrese un numero entero: 3
La suma de los 100 numeros siguientes a 3 es: 5350

# def diecinueve():
# primero ponemos la tasa de cambio, luego pedimos ingresar la cantidad, le damos el valor al dolar de los euros multipl9icado por la tasa de cambio
# luego imprimimos cuantos euros equivalen a cuantos dolares (con un setprecision)

    tasa_cambio = 1.1 
    euros = float(input("Ingrese la cantidad en euros: "))
    dolares = euros * tasa_cambio

    print(f"{euros:.2f} € equivalen a {dolares:.2f} $")

Ingrese la cantidad en euros: 4
4.00 € equivalen a 4.40 $

# def veinte():
# pedimos ingresar la altura y luego la anchura, le damos al area el valor de la altura multiplicado por la anchura
# y finalmente imprimimos el area del rectangulo

    altura = float(input("Ingrese la altura del rectangulo: "))
    anchura = float(input("Ingrese la anchura dedl rectangulo: "))
    area = altura * anchura
    print("El area del rectangulo es:", area)

Ingrese la altura del rectangulo: 3
Ingrese la anchura dedl rectangulo: 4
El area del rectangulo es: 12.0

# def veintiuno():
# primero pedimos ingresar los dos numeros, si n1 es mayor a n2 entonces imprimimos eso, ademas si n2 es mayor a n1 imprimimos eso
# de lo contrario imprimimos que ambos numeros son iguales

    n1 = float(input("Ingrese el priimer numero: "))
    n2 = float(input("Ingrese el segundo numero: "))

    if n1 > n2:
        print(f"El mayor es {n1} y el menor es {n2}")
    elif n2 > n1:
        print(f"El mayor es {n2} y el menor es {n1}")
    else:
        print("Ambos numeros son iguales")

Ingrese el priimer numero: 4
Ingrese el segundo numero: 7
El mayor es 7.0 y el menor es 4.0

# def veintidos():
# primero pedimos que ingrese un numero entero, luego imprimimos que los numeros impares menores que n son en tal rango
# entonces ponemos el rango en el que son los numeros impares, desde uno en adelante de dos en dos hasta el numero elegido
# y por ultimo lo imprimimos

    n = int(input("Ingrese un numero entero: "))
    print(f"Los numeros impares menores que {n} son:")
    
    for i in range (1, n, 2):
        print(i)

Ingrese un numero entero: 10
Los numeros impares menores que 10 son:
1
3
5
7
9

# def veintitres():
# primero pedimos dos numeros enteros, luego ponemos while (mientras) b != 0: (b sea diferente de 0)
# a toma el valor de b y b toma el valor de a dividido a b, entonces en ese bucle se va haciendo mas pequeño hasta llegar a 0 y encontrar el mcd
# luego imprimimos que el mcd es a ya que b tomo el valor de a entre b para encontrar el mcd por lo que a es el mcd

    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))

    while b != 0:
        a, b = b, a % b
    print("El maximo comun divisor es:", a)

Ingrese el primer numero: 3
Ingrese el segundo numero: 6
El maximo comun divisor es: 3

# def veintiseis():
# primero pedimos 3 nummeros enteros, luego ponemos que menor tiene el valor del minimo entre los 3 numero
# y luego ponemos que mayor tiene el valor del maximo entre los 3 y al final imprimos cual es el menos y cual es el mayor y asi 
# tendremos cual sera el menor y mayor entre los 3

    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = int(input("Ingrese el tercer numero: "))

    menor = min(a,b,c)
    mayor = max(a,b,c)
    
    print("El numero menor es:", menor)
    print("El numero mayor es:", mayor)

Ingrese el primer numero: 2
Ingrese el segundo numero: 3
Ingrese el tercer numero: 4
El numero menor es: 2
El numero mayor es: 4

# def veintisiete():
# primero hacemos un bucle con el while en el cual ingresamos la temperatura y con el if si ponemos 999 el programa termina
# luego de infgresar los farenheits ponemos la formula que convierte los f a celcius y luego imprimimos que f equivalen a los celsius con un setprecision

    while True:
        f = float(input("Ingrese una temperatura en °F (999 para salir): "))

        if f == 999:
            print("programa finalizado.")
            break

        c = (f - 32) * 5 / 9
        print(f"{f}°F equivalen a {c:.2f} °C")

Ingrese una temperatura en °F (999 para salir): 666
666.0°F equivalen a 352.22 °C
Ingrese una temperatura en °F (999 para salir): 999
programa finalizado.

# def treinta():
# primero ponemos un for para el rango de 2 a 51, entonces para identificar los numeros primos ponemos que para que sea primo es verdad(True)
# que para el divisor en el rango de 2 hasta el numero, entonces if el numero entre el divisor deja un residuo, si lo hace significa que no seria un numero primo, es_primo = false (falso), ahi termina el bucle entonces if, si es primero pedimos imprimir el num (numero)
    for num in range (2, 51):
        es_primo = True
        for divisor in range(2, num):
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            print(num)

3
5
7
11
13
17
19
23
29
31
37
41
43
47
