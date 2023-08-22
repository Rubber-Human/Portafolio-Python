# Función que calcula el valor futuro de un capital en el presente
def valor_futuro(valor_actual, interes, anios):
    vf = 0
    x = 0
    while x <= anios:
        print(x,"- ", end = "")
        vf = valor_actual*(1+interes/100)**x
        print(vf)
        x += 1

# Función que calcula el valor presente de un capital en el futuro
def valor_actual(valor_futuro, interes, anios):
    va = 0
    x = 0
    while x >= -(anios):
        print(x,"- ", end = "")
        va = valor_futuro/(1+interes/100)**abs(x)
        print(va)
        x -= 1

def main():
      capital = float(input("Introduce un capital ($): "))
      interes = float(input("Introduce un tipo de interés (%): "))
    anios = int(input("Introduce un número de años: "))
    print()
    print("VALOR FUTURO")
    valor_futuro(capital, interes, anios)
    print("VALOR ACTUAL")
    valor_actual(capital, interes, anios)
    
main()
