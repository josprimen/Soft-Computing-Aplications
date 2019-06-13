import math
import numpy as np

nreal = 4
nbin = 0
ncon = 2
number_obj = 2

min_realvar = [0.0, -2.0, -2.0, -2.0]
max_realvar = [1.0, 2.0, 2.0, 2.0]

mysign = lambda x: 1.0 if x > 0 else -1.0


def solution(xreal):

    obj = [np.infty, np.infty]
    constr = [np.infty, np.infty]
    sum1 = 0.0
    sum2 = 0.0

    for j in range(2, nreal+1):
        if j%2 == 1:
            yj = xreal[j-1] - 0.8*xreal[0]*math.cos(6.0*math.pi*xreal[0] + j*math.pi/nreal)
            sum1 = sum1 + (yj*yj)
        else:
            yj = xreal[j-1] - 0.8*xreal[0]*math.sin(6.0*math.pi*xreal[0] + j*math.pi/nreal)
            sum2 = sum2 + (yj*yj)

    obj[0] = xreal[0] + sum1
    obj[1] = (1.0 - xreal[0]) * (1.0 - xreal[0]) + sum2

    constr[0] = xreal[1] - 0.8 * xreal[0] * math.sin(6.0 * xreal[0] * math.pi + 2.0 * math.pi / nreal) - mysign(
        (xreal[0] - 0.5) * (1.0 - xreal[0])) * math.sqrt(math.fabs((xreal[0] - 0.5) * (1.0 - xreal[0])))

    constr[1] = xreal[3] - 0.8 * xreal[0] * math.sin(6.0 * xreal[0] * math.pi + 4.0 * math.pi / nreal) - mysign(
        0.25 * math.sqrt(1 - xreal[0]) - 0.5 * (1.0 - xreal[0])) * math.sqrt(
        math.fabs(0.25 * math.sqrt(1 - xreal[0]) - 0.5 * (1.0 - xreal[0])))

    return obj, constr