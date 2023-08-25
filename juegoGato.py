def printBoard(tablero):
    print('   1    2    3')
    for r in range(3):
        print(f'{r+1} {tablero[r]}')

def putTile(tablero, x, y, ficha):
    coordX = int(x)-1
    coordY = int(y)-1
    
    if coordX < 0 or coordX > 2 or coordY < 0 or coordY > 2:
        print(f'Coordenadas en X,Y incorrectas: {coordX+1},{coordY+1}')
        return tablero
    else:
        if tablero[coordY][coordX] == '':
            if ficha == '0':
                tablero[coordY][coordX] = '0'
            elif ficha == 'X' or ficha == 'x':
                tablero[coordY][coordX] = 'X'
            else:
                print('Error. Introduce un valor correcto')
            return tablero
        else:
            print('Esta celda ya está ocupada')
            return tablero

def checkWinner(tablero, conteo):
    for m in range(3):
        for n in range(3):
            if tablero[m][n] != '':
                conteo += 1
            if conteo == 9:
                print('Fin del juego')
                return False, conteo
            else:
                return True, conteo

def main():
    filas = 3
    columnas = 3
    coordX = 0
    coordY = 0
    ficha = ''
    juegoActivo = True
    celdasOcupadas = 0

    tablero = [['']*columnas for i in range (filas)]

    printBoard(tablero)

    while(juegoActivo):
    
        coordX = input('Introduce la coordenada X del 1 al 3: ')
        coordY = input('Introduce la coordenada Y del 1 al 3: ')
        ficha = input('Introduce 0 para círculo o X para cruz: ')

        tablero = putTile(tablero, coordX, coordY, ficha)

        printBoard(tablero)
        juegoActivo, celdasOcupadas = checkWinner(tablero, celdasOcupadas)
