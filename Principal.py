import numpy as np
import itertools
import zdt3

class principal:

    def __init__(self):
        self.population_size = 30
        self.generations = 10.000
        self.neighborhood_size = 0.2 #Probar con 0.3
        self.sig = 20 #SIG para desviación estandar
        self.pr = 0.5 #Operador de mutación gaussiana
        self.f = 0.5 #mutación
        self.cr = 0.5 #cruce
        self.born = False #Para saber si es la primera
        self.population = []
        self.weights = []
        self.distances = []
        self.neighbors = [list() for _ in range(self.population_size)]
        self.t = 30 #Porcentaje de vecindad ??
        self.obj = zdt3.zdt3()
        self.best = [np.infty for _ in range(self.obj.number_obj)]


    def first(self):
        #self.population = [np.random.uniform(0, 1)] generalicemos
        self.population = [[np.random.uniform(self.obj.min_realvar[i], self.obj.max_realvar[i])
            for i in range(30)] for _ in range(self.population_size)]  #Generalizar el 30?

        self.weights = np.random.dirichlet(
            np.ones(self.obj.number_obj), self.population_size)

        self.distances = {(x, y): np.linalg.norm(self.weights[x]-self.weights[y])
                          for x, y in itertools.product(list(range(len(self.weights))), repeat=2)}

        self.best = [np.min([self.obj.value(individual)[i] for individual in self.population])
                     for i in range(self.obj.number_obj)]

        self.born = True

        self.compute_neighbors()

    def process(self):
        self.birth() #Hemos de iniciar con una primera población y datos
        for generation in range(self.generations):
            for i in range(self.population_size):
                if self.reproduce(i) != -1:
                    obj = self.evaluate(self.population[i])
                    for j in range(self.obj.number_obj):
                        if self.best[j] > obj[j]:
                            self.best[j] = obj[j]
                    tchebycheff_son = max([self.weights[i][j] * np.abs(
                        obj[j] - self.best[j])
                        for j in range(self.obj.number_obj)])
                    for j in self.neighbors[i]:
                        obj_neighbor = self.evaluate(self.population[j])
                        tchebycheff_neighbor = max([self.weights[j][k] * np.abs(
                            obj_neighbor[k] - self.best[k])
                                                    for k in range(self.obj.number_obj)])
                        if tchebycheff_son <= tchebycheff_neighbor:
                            self.population[j] = self.population[i]

    def compute_neighbors(self):
        for i in range(self.population_size):
            candidates = {y: self.distances[(x, y)]
                          for (x, y) in self.distances.keys() if x == i}
            candidates = sorted(candidates.items(), key=lambda x: x[1])
            c = [candidates[x][0] for x in range(len(candidates))]
            neighbors = c[:int(np.floor(
                self.population_size * self.neighborhood_size))]
            self.neighbors[i] = neighbors

    #Darle un repaso y comparar operadores geneticos
    def reproduce(self, individual):
        if (np.random.random() > self.cr):
            a = self.neighbors[individual]
            parents = np.random.choice(a, 3, replace=False)
            self.weights[individual] = self.weights[parents[0]] + self.f * (
                    self.weights[parents[1]] - self.weights[parents[2]])
            return individual
        return -1


    def evaluate(self, individual):
        return self.obj.solution(individual)