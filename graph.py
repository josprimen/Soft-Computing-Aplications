import Principal
import numpy as np
import matplotlib.pyplot as plt
import zdt3

class testeo():

    def test(self):
        program = Principal.Principal()
        program.process()
        values = np.array([zdt3.zdt3().solution(program.population[j])
                           for j in range(program.population_size)])
        x, y = values.T
        plt.scatter(x, y)
        plt.show()
        return program
