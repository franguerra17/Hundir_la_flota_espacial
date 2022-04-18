'''
Fecha: 14/04/2022
Objetivo: Creación de tableros para Hundir La Flota
'''
import numpy as np
import random

tablero = np.full((10, 10), (' '))
tableroJug = np.full((10, 10), (' '))

#Función para comprobar si es un entero
def comprobar_int(num):
    num = int(num)
    #Arreglar esta funciíon para comprobar si es un entero


#Función para definir si el tablero es agua o la posición está ocupada
def space(x, y):
    if tablero[x][y] == ' ':
        return True
    else:
        return False
#Función para definir si el tablero del jugador es agua o la posición está ocupada
def space_man(x, y):
    if tableroJug[x][y] == ' ':
        return True
    else:
        return False

#Función para comprobar los límites del tablero
def limit(num1, num2,):
    if num1 >= 0 and num1 <= 9 and num2 >= 0 and num2 <= 9:
        return True
    else: 
        return False

#Funciones para crer una 'x' y una 'y' aleatoria
def x_aleatoria():
    return random.randint(0, 9)

def y_aleatoria():   
    return random.randint(0, 9)

#Funciones para crear barcos aleatorios según su dimensión
def crea_crucero(tablero):

    #Orientación. norte->1  sur->2  este->3  oeste-->4
    orientacion = random.randint(1, 5)

    if orientacion == 1: #Dirección Norte
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            x1 = x+1
            x2 = x+2
            x3 = x+3

            if limit(x, y) and limit(x1, y) and limit(x2, y) and limit(x3, y) and space(x, y) and space(x1, y) and space(x2, y) and space(x3, y):
                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    tablero[x2][y] = 'O'
                    tablero[x3][y] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()
                    
    elif orientacion == 2: #Dirección Sur
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            x1 = x-1
            x2 = x-2
            x3 = x-3

            if limit(x, y) and limit(x1, y) and limit(x2, y) and limit(x3, y) and space(x, y) and space(x1, y) and space(x2, y) and space(x3, y):

                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    tablero[x2][y] = 'O'
                    tablero[x3][y] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()

    elif orientacion == 3: #Dirección Este
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            y1 = y+1
            y2 = y+2
            y3 = y+3

            if limit(x, y) and limit(x, y1) and limit(x, y2) and limit(x, y3) and space(x, y) and space(x, y1) and space(x, y2) and space(x, y3):

                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    tablero[x][y2] = 'O'
                    tablero[x][y3] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()
    else: #Dirección Oeste
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            y1 = y-1
            y2 = y-2
            y3 = y-3

            if limit(x, y) and limit(x, y1) and limit(x, y2) and limit(x, y3) and space(x, y) and space(x, y1) and space(x, y2) and space(x, y3):

                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    tablero[x][y2] = 'O'
                    tablero[x][y3] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()
    return (tablero)

def crea_lanzadera(tablero):

    #Orientación. norte->1  sur->2  este->3  oeste-->4
    orientacion = random.randint(1, 5)

    if orientacion == 1: #Dirección Norte
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            x1 = x+1
            x2 = x+2

            if limit(x, y) and limit(x1, y) and limit(x2, y) and space(x, y) and space(x1, y) and space(x2, y):
                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    tablero[x2][y] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()
                    
    elif orientacion == 2: #Dirección Sur
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            x1 = x-1
            x2 = x-2

            if limit(x, y) and limit(x1, y) and limit(x2, y) and space(x, y) and space(x1, y) and space(x2, y):
                
                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    tablero[x2][y] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()

    elif orientacion == 3: #Dirección Este
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            y1 = y+1
            y2 = y+2

            if limit(x, y) and limit(x, y1) and limit(x, y2) and space(x, y) and space(x, y1) and space(x, y2):

                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    tablero[x][y2] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()
    else: #Dirección Oeste
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            y1 = y-1
            y2 = y-2

            if limit(x, y) and limit(x, y1) and limit(x, y2) and space(x, y) and space(x, y1) and space(x, y2):
                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    tablero[x][y2] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()
    return (tablero)

def crea_bombardero(tablero):   

    #Orientación. norte->1  sur->2  este->3  oeste-->4
    orientacion = random.randint(1, 5)

    if orientacion == 1: #Dirección Norte
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            x1 = x+1

            if limit(x, y) and limit(x1, y) and space(x, y) and space(x1, y):
                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()
                    
    elif orientacion == 2: #Dirección Sur
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            x1 = x-1

            if limit(x, y) and limit(x1, y) and space(x, y) and space(x1, y):
                
                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()

    elif orientacion == 3: #Dirección Este
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            y1 = y+1

            if limit(x, y) and limit(x, y1) and space(x, y) and space(x, y1):
                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()
    else: #Dirección Oeste
        while True:
            x = x_aleatoria()
            y = y_aleatoria()
            y1 = y-1

            if limit(x, y) and limit(x, y1) and space(x, y) and space(x, y1):

                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    break
                    
                except IndexError:
                    x = x_aleatoria()
                    y = y_aleatoria()
    return (tablero)

def crea_caza(tablero):

    while True:
        x = x_aleatoria()
        y = y_aleatoria()

        if limit(x, y) and space(x, y):
            try:
                tablero[x][y] = 'O'
                break
                
            except IndexError:
                x = x_aleatoria()
                y = y_aleatoria()
                    
    
    return (tablero)

#Funciones para crear barcos manualmente según su dimensión

def crea_cruceroManual(tablero):

    #Orientación. norte->1  sur->2  este->3  oeste-->4
    orientacion = input('Introduciendo Crucero, tamaño = 4. indique que direcciíon quiere que crezca el barco: norte, sur este u oeste: ').lower()
    while True:
        if orientacion == 'norte' or orientacion == 'sur' or orientacion == 'este' or orientacion == 'oeste':
            break
        else:
            orientacion = input('indique que direcciíon quiere que crezca el Crucero, tamaño = 4: norte, sur este u oeste: ').lower()

    if orientacion == 'norte': #Dirección Norte
        while True:
            x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
            
            y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
            
            x1 = x+1
            x2 = x+2
            x3 = x+3

            if limit(x, y) and limit(x1, y) and limit(x2, y) and limit(x3, y) and space_man(x, y) and space_man(x1, y) and space_man(x2, y) and space_man(x3, y):
                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    tablero[x2][y] = 'O'
                    tablero[x3][y] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
                    y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)

    elif orientacion == 'sur': #Dirección Sur
        while True:
            x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')

            y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
            x1 = x-1
            x2 = x-2
            x3 = x-3

            if limit(x, y) and limit(x1, y) and limit(x2, y) and limit(x3, y) and space_man(x, y) and space_man(x1, y) and space_man(x2, y) and space_man(x3, y):
                
                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    tablero[x2][y] = 'O'
                    tablero[x3][y] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
                    y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)

    elif orientacion == 'este': #Dirección Este
        while True:
            x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
                    
            y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
            y1 = y+1
            y2 = y+2
            y3 = y+3

            if limit(x, y) and limit(x, y1) and limit(x, y2) and limit(x, y3) and space_man(x, y) and space_man(x, y1) and space_man(x, y2) and space_man(x, y3):

                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    tablero[x][y2] = 'O'
                    tablero[x][y3] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
                    y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)

    else: #Dirección Oeste
        while True:
            x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')

            y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
            y1 = y-1
            y2 = y-2
            y3 = y-3

            if limit(x, y) and limit(x, y1) and limit(x, y2) and limit(x, y3) and space_man(x, y) and space_man(x, y1) and space_man(x, y2) and space_man(x, y3):
                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    tablero[x][y2] = 'O'
                    tablero[x][y3] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para el Crucero, tamaño = 4: ')
                    y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para el Crucero, tamaño = 4: ')

            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)

    return (tablero)

def crea_lanzaderaManual(tablero):

    #Orientación. norte->1  sur->2  este->3  oeste-->4
    orientacion = input('indique que direcciíon quiere que crezca la Lanzadera tamaño = 3: norte, sur este u oeste: ').lower()
    while True:
        if orientacion == 'norte' or orientacion == 'sur' or orientacion == 'este' or orientacion == 'oeste':
            break
        else:
            orientacion = input('indique que direcciíon quiere que crezca la Lanzadera tamaño = 3: norte, sur este u oeste: ').lower()

    if orientacion == 'norte': #Dirección Norte
        while True:
            x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')

            y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
            x1 = x+1
            x2 = x+2

            if limit(x, y) and limit(x1, y) and limit(x2, y) and space_man(x, y) and space_man(x1, y) and space_man(x2, y):
                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    tablero[x2][y] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
                    y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)
                    
    elif orientacion == 'sur': #Dirección Sur
        while True:
            x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')

            y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
            x1 = x-1
            x2 = x-2

            if limit(x, y) and limit(x1, y) and limit(x2, y) and space_man(x, y) and space_man(x1, y) and space_man(x2, y):
                
                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    tablero[x2][y] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
                    y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')

            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)

    elif orientacion == 'este': #Dirección Este
        while True:
            x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')

            y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
            y1 = y+1
            y2 = y+2

            if limit(x, y) and limit(x, y1) and limit(x, y2) and space_man(x, y) and space_man(x, y1) and space_man(x, y2):

                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    tablero[x][y2] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
                    y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')

            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)

    else: #Dirección Oeste
        while True:
            x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')

            y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
            y1 = y-1
            y2 = y-2

            if limit(x, y) and limit(x, y1) and limit(x, y2) and space_man(x, y) and space_man(x, y1) and space_man(x, y2):
                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    tablero[x][y2] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para la Lanzadera, tamaño = 3: ')
                    y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para la Lanzadera, tamaño = 3: ')

            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)

    return (tablero)

def crea_bombarderoManual(tablero):

    #Orientación. norte->1  sur->2  este->3  oeste-->4
    orientacion = input('indique que direcciíon quiere que crezca el Bombardero tamaño=2: norte, sur este u oeste: ').lower()
    while True:
        if orientacion == 'norte' or orientacion == 'sur' or orientacion == 'este' or orientacion == 'oeste':
            break
        else:
            orientacion = input('indique que direcciíon quiere que crezca el Bombardero tamaño=2: norte, sur este u oeste: ').lower()

    if orientacion == 'norte': #Dirección Norte
        while True:
            x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
            y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
            x1 = x+1

            if limit(x, y) and limit(x1, y) and space_man(x, y) and space_man(x1, y):
                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
                    y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')

            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)
                    
    elif orientacion == 'sur': #Dirección Sur
        while True:
            x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')

            y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
            x1 = x-1

            if limit(x, y) and limit(x1, y) and space_man(x, y) and space_man(x1, y):
                
                try:
                    tablero[x][y] = 'O'
                    tablero[x1][y] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')

                    y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)

    elif orientacion == 'este': #Dirección Este
        while True:
            x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
            y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
            y1 = y+1

            if limit(x, y) and limit(x, y1) and space_man(x, y) and space_man(x, y1):

                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
                    y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')

            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)

    else: #Dirección Oeste
        while True:
            x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
            while 1>0:
                try:
                    x = int(x)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')

            y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
            while 1>0:
                try:
                    y = int(y)
                    break
                except:
                    print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                    y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
            y1 = y+1

            if limit(x, y) and limit(x, y1) and space_man(x, y) and space_man(x, y1):
                try:
                    tablero[x][y] = 'O'
                    tablero[x][y1] = 'O'
                    print(tablero)
                    break
                    
                except IndexError:
                    x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
                    while 1>0:
                        try:
                            x = int(x)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            x = input('Introduzca la coordenada "x" para el Bombardero, tamaño = 2: ')
                    y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')
                    while 1>0:
                        try:
                            y = int(y)
                            break
                        except:
                            print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                            y = input('Introduzca la coordenada "y" para el Bombardero, tamaño = 2: ')

            else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)

    return (tablero)

def crea_cazaManual(tablero):

    while True:
        x = input('Introduzca la coordenada "x" para el Caza, tamaño = 1: ')
        while 1>0:
            try:
                x = int(x)
                break
            except:
                print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                x = input('Introduzca la coordenada "x" para el Caza, tamaño = 1: ')

        y = input('Introduzca la coordenada "y" para el Caza, tamaño = 1: ')
        while 1>0:
            try:
                y = int(y)
                break
            except:
                print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                y = input('Introduzca la coordenada "y" para el Caza, tamaño = 1: ')
        if limit(x, y) and space_man(x, y):
            try:
                tablero[x][y] = 'O'
                print(tablero)
                break
                
            except IndexError:
                x = input('Introduzca la coordenada "x" para el Caza, tamaño = 1: ')
                while 1>0:
                    try:
                        x = int(x)
                        break
                    except:
                        print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                        x = input('Introduzca la coordenada "x" para el Caza, tamaño = 1: ')
                y = input('Introduzca la coordenada "y" para el Caza, tamaño = 1: ')
                while 1>0:
                    try:
                        y = int(y)
                        break
                    except:
                        print('Vaya, ha habido un error', '\U0001F615', 'inténtelo de nuevo')
                        y = input('Introduzca la coordenada "y" para el Caza, tamaño = 1: ')

        else:
                print('Las coordenadas intorucidas no son correctas, intente unas coordenadas dentro del tablero y que no pise a otra nave')
                print(tablero)
    
    return (tablero)

# Función para colocar x numeros de barcos según el tamaño del barco
def num_naves(n, CreaNave, tablero):
    contador1 = 0
    while contador1 < n:
        CreaNave(tablero)
        contador1 += 1

#Funcion busca corrdenada
def busca_coor(x, y, array, array_disparos):
    if limit(x,y):
        if array[x][y] == ' ':
            print('Se ha perdido en el vacío, sigue probando')
            array_disparos[x][y] == '-'
        elif array[x][y] == 'O':
            print('¡El disparo ha dado en el blanco! Vuelve a disparar')
            array_disparos[x][y] == 'X'
        else: print('Ahí solo quedan restos de un disparo anterior')
        
        return array_disparos
    else:
        print('La coordenada elegida está fuera de los límites del tablero.Has disparado a una reserva que está lleno de osos espaciales en peligro de extinción PIERDE EL TURNO')

