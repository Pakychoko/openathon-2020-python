# Supongamos que tenemos una lista de numeros del 1 al 100. 
# Te propongo obtener la lista sólo de aquellos números pares. 
# Haz una versión con list comprehension y otra sin ella.


# Without List comprehension
lista = []
for i in range(100):
    lista.append(i)

print("Tenemos la lista: ")
print(lista)

resultado = []
for i in lista:
    if i%2 == 0:
        resultado.append(i)

print("Tenemos la lista de pares: ")
print(resultado)

# List comprehenension
lista = [i for i in range(100)]
print("Tenemos la lista con list comprehension: ")
print(lista)

resultado = [i for i in lista if i%2 == 0]
print("Tenemos la lista de pares con list comprehension: ")
print(resultado)