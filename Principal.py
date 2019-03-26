import numpy as np
import itertools
import zdt3

class principal:

    def __init__(self):
        population_size = 30
        generations = 10.000
        neighborhood_size = 0.2 #Probar con 0.3
        sig = 20
        pr = 0.5
        f = 0.5
        cr = 0.5
        born = False #Para saber si es la primera
        population = []
        weights = []
        distances = []
        neighbors = [list() for _ in range(self.population_size)]
        t = 30 #Porcentaje de vecindad ??
        obj = zdt3.zdt3()
        best = [np.infty for _ in range(self.obj.number_obj)]


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


    def compute_neighbors(self):
        for i in range(self.population_size):
            candidates = {y: self.distances[(x, y)]
                          for (x, y) in self.distances.keys() if x == i}
            candidates = sorted(candidates.items(), key=lambda x: x[1])
            c = [candidates[x][0] for x in range(len(candidates))]
            neighbors = c[:int(np.floor(
                self.population_size * self.neighborhood_size))]
            self.neighbors[i] = neighbors