import Principal
import numpy as np
import matplotlib.pyplot as plt
import zdt3

class testeo():

    def test(self):
        program = Principal.Principal()
        program.process()
        values = np.array([zdt3.solution(program.population[j])
                           for j in range(program.population_size)])
        x, y = values.T
        plt.scatter(x, y)
        plt.show()
        return program

    #grafica.test_moec(100, 100, False) -> sin primera generacion
    #grafica.test_moec(100, 100, True) -> con primera generación (no fallos)
    def test_moec(self, p_size, n_gen, all_gen):
        m = Principal.Principal(p_size, n_gen, all_gen)
        m.process()
        self.last_gen_obj(m)
        self.all_gen_obj(m)
        self.first_gen_obj(m)
        return m

    def last_gen_obj(self, moec):
        with open('results/last_gen_obj_moec_' + str(moec.population_size) + '_'
                  + str(moec.generations) + '.out', 'w') as f:
            for i in range(moec.population_size):
                obj = zdt3.solution(moec.population[i])
                f.write('{:.6e}'.format(obj[0]) + '\t'
                        + '{:.6e}'.format(obj[1]) + '\n')

    def all_gen_obj(self, moec):
        with open('results/all_gen_obj_moec_' + str(moec.population_size) + '_'
                  + str(moec.generations) + '.out', 'w') as f:
            for i in range(len(moec.bol_gen)):
                obj = zdt3.solution(moec.bol_gen[i])
                f.write('{:.6e}'.format(obj[0]) + '\t'
                        + '{:.6e}'.format(obj[1]) + '\n')

    def first_gen_obj(self, moec):
        with open('results/first_gen_obj_moec_' + str(moec.population_size) + '_'
                  + str(moec.generations) + '.out', 'w') as f:
            '''print('Tamaño de la poblacion')
            print(moec.population_size)'''
            for i in range(moec.population_size):
                '''print('Cosa')
                print(moec.bol_gen[i])'''
                obj = zdt3.solution(moec.bol_gen[i])
                f.write('{:.6e}'.format(obj[0]) + '\t'
                        + '{:.6e}'.format(obj[1]) + '\n')
