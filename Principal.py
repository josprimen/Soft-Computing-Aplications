import numpy as np
class principal:

    def __init__(self):
        population_size = 30
        generations = 10.000
        population = []
        weights = []
        distances = []
        neighbors = []
        t = 30 #Porcentaje de vecindad ??

    def first(self):
        self.population = [np.random.uniform(0, 1)]
        self.weights = np.random.dirichlet(
            np.ones(self.population_size), size=1)
        #self.distances = ?

    def process(self):
        for generation in range(self.generations):
            for i in range(self.population_size):
                self.evolutive_operatos()
                self.evaluate()
                self.selection()
                self.propagation()
