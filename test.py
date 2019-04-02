import Principal
import numpy as np
import matplotlib.pyplot as plt
import zdt3


def test_moec(p_size, n_gen, all_gen):
    m = Principal.Principal(p_size, n_gen, all_gen)
    m.process()
    last_gen_obj(m)
    all_gen_obj(m)
    return m


def last_gen_obj(moec):
    with open('tests/last_gen_obj_moec_' + str(moec.population_size) + '_'
              + str(moec.generations) + '.out', 'w') as f:
        for i in range(moec.population_size):
            obj = zdt3.solution(moec.population[i])
            f.write('{:.6e}'.format(obj[0]) + '\t'
                    + '{:.6e}'.format(obj[1]) + '\n')

def all_gen_obj(moec):
    with open('tests/all_gen_obj_moec_' + str(moec.population_size) + '_'
              + str(moec.generations) + '.out', 'w') as f:
        for i in range(len(moec.bol_gen)):
            obj = zdt3.solution(moec.bol_gen[i])
            f.write('{:.6e}'.format(obj[0]) + '\t'
                    + '{:.6e}'.format(obj[1]) + '\n')


def test():
    m = Principal.Principal()
    m.process()
    values = np.array([zdt3.solution(m.population[j])
                       for j in range(m.population_size)])
    x, y = values.T
    plt.scatter(x, y)
    plt.show()
    return m
