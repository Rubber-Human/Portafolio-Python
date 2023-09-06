def fibonacci (num):
    suma_fibo = 0
    lista_fibo = [1]
    for i in range (0, num):
        suma_fibo += lista_fibo[i-1]
        lista_fibo.append(suma_fibo)
    return lista_fibo[num]
    
print (fibonacci(5000))
