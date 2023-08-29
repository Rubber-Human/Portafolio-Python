# Prueba Feez Buzz
# El programa debe imprimir los números del 1 al 100
# y si un número es múltiplo de 3, deberá imprimir "Feez",
# si es múltiplo de 5, deberá imprimir "Buzz"
# y si es múltiplo de 3 y 5, deberá imprimir "Feez Buzz"

lista = [n for n in range (1,101)]

for i in range(0,100):
    # Evalúa si el valor de la lista es de tipo string para evitar que intente realizar
    # una operación matemática en un texto y que arroje un error
    if (type(lista[i]) == str):
        pass
    # Si el valor es múltiplo de 3 y de 5 al mismo tiempo (es decir, valores múltiplos de 15),
    # cambia el contenido por "Feez Buzz"
    elif lista[i] % 3 == 0 and lista[i] % 5 == 0:
        lista[i] = "Feez Buzz"
    # Si el valor es múltiplo de 3, cambia su contenido por "Feez"
    elif (lista[i] % 3 == 0):
        lista[i] = "Feez"
    # Si el valor es múltiplo de 5, cambia su contenido por "Buzz"
    elif (lista[i] % 5 == 0):
        lista[i] = "Buzz"
    # Imprime toda la lista, incluyendo su valor original
    print(f"{i+1} - {lista[i]}")
