# En el laboratorio anterior resolvimos un problema que consistia en crear una lista de numeros pares del 1 al 100 a partir de otra. 
# Te propongo crear una función que indique si un número es par o no, y la utilices en la solución anterior. 
# Puedes hacer lo mismo pero con números impares definiendo una función lambda

lista = [i for i in range(100)]

def isPar(num):
    if num % 2 == 0:
        print("{} es par".format(i))
    else:
        print("{} no es par".format(i))

for i in lista:
    isPar(i)


isNones = lambda n : n % 2 != 0

for i in lista:
    if(isNones(i)):
        print("{} es impar".format(i))
    else:
        print("{} no es impar".format(i))
    