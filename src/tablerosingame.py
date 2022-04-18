import numpy as np

#import tablerosiniciales


def tableroingame():
    tablero1 = tablerosInciales.crear_tablero()
    tablero2 = tablerosInciales.crear_tablero()

    tablerojugador = tablero1.copy()
    tablerocomputadora = tablero2.copy()
    tablerovacio1 = np.full((10, 10), ' ')
    tablerovacio2 = np.full((10, 10), ' ')
    return (tablerojugador, tablerocomputadora, tablerovacio1, tablerovacio2)