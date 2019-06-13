import Principal
import numpy as np
import matplotlib.pyplot as plt
import zdt3
import cf6

class testeo():

    def test(self, p_size, n_gen, constr, all_gen):
        if constr:
            f = open("PF.dat", "r")
            a, b = [], []
            for line in f:
                a1, a2 = line.strip().split("\t")
                a.append(float(a1))
                b.append(float(a2))
            program = Principal.Principal(p_size, n_gen, constr, all_gen)
            program.process()
            values = np.array([cf6.solution(program.population[j])
                               for j in range(program.population_size)])
            x, y = values.T
            plt.scatter(x, y)
            plt.scatter(a, b, c="red", alpha=0.05)
            plt.show()
            return program
        else:
            f = open("frente.dat", "r")
            a, b = [], []
            for line in f:
                a1, a2 = line.strip().split("\t")
                a.append(float(a1))
                b.append(float(a2))
            program = Principal.Principal(p_size, n_gen, constr, all_gen)
            program.process()
            values = np.array([zdt3.solution(program.population[j])
                           for j in range(program.population_size)])
            x, y = values.T
            plt.scatter(x, y)
            plt.scatter(a, b, c="red", alpha=0.1)
            plt.show()
            return program

    #Inicialización grafica = testeo()

    #Imprimir los datos
    #grafica.test_moec(100, 100, False, False) -> sin primera generacion zdt3
    #grafica.test_moec(100, 100, True, False) -> sin primera generacion cf6
    #grafica.test_moec(100, 100, False, True) -> con primera generación (no fallos) zdt3
    #grafica.test_moec(100, 100, True, True) -> con primera generación (no fallos) cf6


    #Imprimir las graficas
    #grafica.test(100,100,False,False) -> ultimo parametro irrelevante zdt3
    #grafica.test(100,100,True,False) -> ultimo parametro irrelevante cf6

    def test_moec(self, p_size, n_gen, constr, all_gen):
        m = Principal.Principal(p_size, n_gen, constr, all_gen)
        m.process()
        if constr:
            self.last_gen_obj_c(m)
            self.all_gen_obj_c(m)
        else:
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

    def last_gen_obj_c(self, moec):
        with open('results/last_gen_obj_cmoec_' + str(moec.population_size) + '_'
                  + str(moec.generations) + '.out', 'w') as f:
            for i in range(moec.population_size):
                (v, c) = cf6.solution(moec.population[i])
                obj = [v[j] + c[j] for j in range(cf6.number_obj)]
                f.write('{:.6e}'.format(obj[0]) + '\t'
                        + '{:.6e}'.format(obj[1]) + '\n')

    def all_gen_obj_c(self, moec):
        with open('results/all_gen_obj_cmoec_' + str(moec.population_size) + '_'
                  + str(moec.generations) + '.out', 'w') as f:
            for i in range(len(moec.bol_gen)):
                (v, c) = cf6.solution(moec.bol_gen[i])
                obj = [v[j] + c[j] for j in range(cf6.number_obj)]
                f.write('{:.6e}'.format(obj[0]) + '\t'
                        + '{:.6e}'.format(obj[1]) + '\n')
