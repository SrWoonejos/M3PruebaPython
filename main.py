#PRUEBA M3 - INTRODUCCION A PYTHON3

#lista nombres
nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

#funcion para magos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = 'El gran ' + magos[i]

#funcion nombres lista
def print_nombres(lista):
    for nombre in lista:
        print(nombre)

#separar nombres en categorias
def nombre_grupos(nombres):
    magos = []
    cientificos = []
    otros = []

for nombre in nombres:
    if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
        magos.append(nombre)
    elif nombre in ['Newton', 'Hawking', 'Einstein']:
        cientificos.append(nombre)
    else:
        otros.apprend(nombre)

return magos, cientificos, otros

#imprimir lista completa
print("Lista completa: ")
print_nombres(nombres)

#separar nombres
magos, cientificos, otros = nombre_grupos(nombres)