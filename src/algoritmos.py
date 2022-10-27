import math


def distancia_euclidiana(x_1, y_1, x_2, y_2):
    """ Devuelve el resultado de la distancia euclidiana """
    """ 
        x_1 -- origen x
        x_2 -- destino x
        y_1 -- origen y
        y-2 -- destino y
     """
    return math.sqrt(pow(x_2 - x_1, 2) + pow(y_2-y_1, 2))
