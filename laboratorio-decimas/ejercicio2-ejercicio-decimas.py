import random
import operator
n1 = int(input("Filas matriz 1 "))
m1 = int(input("Columnas matriz 1 "))

matriz1 = []
for i in range(n1):
    aux = []
    for j in range(m1):
        aux.append(random.randint(0,5))
    matriz1.append(aux)

n2 = int(input("Filas matriz 2 "))
m2 = int(input("Columnas matriz 2 "))
matriz2 = []
for i in range(n2):
    aux = []
    for j in range(m2):
        aux.append(random.randint(0,5))
    matriz2.append(aux)

print(f"1 {matriz1}")
print(f"2 {matriz2}")

def suma(c,d):
    if len(c) != len(d) or len(c[0]) != len(d[0]):
        return "No se pueden sumar matrices de distinto tamaño."
    else:
        matriz3 = []
        for i in range(len(c)):
            aux = []
            for j in range(len(c[0])):
                aux.append(operator.add(c[i][j],d[i][j]))
            matriz3.append(aux)
        return matriz3

def resta(c,d):
    if len(c) != len(d) or len(c[0]) != len(d[0]):
        return "No se pueden restar matrices de distinto tamaño."
    else:
        matriz3 = []
        for i in range(len(c)):
            aux = []
            for j in range(len(c[0])):
                aux.append(operator.sub(c[i][j],d[i][j]))
            matriz3.append(aux)
        return matriz3
    
print(suma(matriz1,matriz2))
print(resta(matriz1,matriz2))
