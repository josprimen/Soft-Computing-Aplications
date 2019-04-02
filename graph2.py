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

    def test_principal(self, populat, generat, bol_gen):
        program = Principal.Principal(populat, generat, bol_gen)
        program.process()
        self.last_gen_obj(program)
        self.all_gen_obj(program)
        return program

    def last_gen_obj(self, program):
        with open('results/last_gen_obj_moec_' + str(program.population_size) + '_'
                  + str(program.generations) + '.out', 'w') as f:
            for i in range(program.population_size):
                obj = zdt3.zdt3().solution(program.population[i])
                f.write('{:.6e}'.format(obj[0]) + '\t'
                        + '{:.6e}'.format(obj[1]) + '\n')

    def all_gen_obj(self, program):
        with open('results/all_gen_obj_moec_' + str(program.population_size) + '_'
                  + str(program.generations) + '.out', 'w') as f:
            for i in range(len(program.list_all_gen)):
                obj = zdt3.zdt3().solution(program.list_all_gen[i])
                f.write('{:.6e}'.format(obj[0]) + '\t'
                        + '{:.6e}'.format(obj[1]) + '\n')

