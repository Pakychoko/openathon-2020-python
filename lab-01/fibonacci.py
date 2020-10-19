# Este programa calcula la lista de numeros de fibonacci

# Variable inicializadas
entrada = 10
i = 0
x = 0
y = 1

# diccionario
fibonacci = {} # la salida sería [1,2,3,5,8]

'''
Aqui calculamos los numeros de Fibonacci
'''
while i < entrada:
    z = y + x
    x = y
    y = z
    i += 1
    fibonacci[i] = y

'''
Aqui formateamos la salida para mostrarla
'''
string = "La lista de numeros de fibonacci es: ["

for clave, valor in fibonacci.items():
    string = string + "{}"
    string = string.format(valor)
    if clave < len(fibonacci):
        string = string + ","
    else:
        string = string + "]"

print(string)



