import math
import numpy as np

class zdt3:

# Inicializamos la clase con los valores del espacio de búsqueda

    def __init__(self):
        self.min_realvar = [0.0 for _ in range(30)]
        self.max_realvar = [1.0 for _ in range(30)]
        self.obj = [np.infty, np.infty]
        self.number_obj = 2

# Creamos la función para obtención de resultados

    def solution(self, xreal):
        n = 30
        tmp = 0.0
        self.obj[0] = xreal[0]
        for i in range(1, n):
            tmp = tmp + xreal[i]
        g = 1 + (9/(n-1)) * tmp
        h = 1 - math.sqrt(xreal[0]/g) - (xreal[0]/g)*math.sin(10*math.pi*xreal[0])

        self.obj[1] = g*h
        return self.obj