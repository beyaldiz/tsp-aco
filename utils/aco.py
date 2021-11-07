import numpy as np
from tqdm import tqdm

from utils.data import Data


class Environment(Data):
    def __init__(self, filename, num_ants, alpha, beta,
                    pheromone_evaporation, estimated_len, num_iters):
        super(Environment, self).__init__(filename)

        self.num_ants = num_ants
        self.alpha = alpha
        self.beta = beta
        self.pheromone_evaporation = pheromone_evaporation
        self.estimated_len = estimated_len
        self.num_iters = num_iters
        self.pheromone = np.ones((self.n, self.n))
        self.best_path = []
        self.best_path_length = np.inf
        self.best_path_length_history = []
        self.ants = []
        for _ in range(num_ants):
            self.ants.append(Ant(self, np.random.choice(self.n),
                                 self.alpha, self.beta))

    def evaporate_pheromone(self):
        self.pheromone *= (1 - self.pheromone_evaporation)
    
    def run(self):
        for i in tqdm(range(self.num_iters)):
            for ant in self.ants:
                ant.cycle()
            self.evaporate_pheromone()
            for ant in self.ants:
                ant.deposit_pheromone()
                ant.reset()
            self.best_path_length_history.append(self.best_path_length)

class Ant:
    def __init__(self, environment, initial_pos, alpha, beta):
        self.env = environment
        self.initial_pos = initial_pos
        self.current_pos = initial_pos
        self.alpha = alpha
        self.beta = beta
        self.path = []
        self.path_length = 0
        self.visited = [False for _ in range(self.env.n)]
        self.visited[initial_pos] = True
    
    def step(self):
        prob_scores = (self.env.pheromone[self.current_pos] ** self.alpha) \
                        * ((1 / self.env.edges[self.current_pos]) ** self.beta)
        prob_scores[self.visited] = 0.0
        prob = prob_scores / np.sum(prob_scores)
        next_pos = np.random.choice(self.env.n, p=prob)
        self.path.append(next_pos)
        self.visited[next_pos] = True
        self.path_length += self.env.edges[self.current_pos, next_pos]
        self.current_pos = next_pos
    
    def cycle(self):
        for i in range(self.env.n - 1):
            self.step()
        self.path_length += self.env.edges[self.current_pos, self.initial_pos]
        if self.env.best_path_length > self.path_length:
            self.env.best_path = self.path
            self.env.best_path_length = self.path_length

    def deposit_pheromone(self):
        for i in range(len(self.path) - 1):
            self.env.pheromone[self.path[i], self.path[i + 1]] += \
                            self.env.estimated_len / self.path_length
            self.env.pheromone[self.path[i + 1], self.path[i]] += \
                            self.env.estimated_len / self.path_length
        self.env.pheromone[self.path[-1], self.path[0]] += \
                            self.env.estimated_len / self.path_length
        self.env.pheromone[self.path[0], self.path[-1]] += \
                            self.env.estimated_len / self.path_length

    def reset(self):
        self.current_pos = self.initial_pos
        self.path = []
        self.path_length = 0
        self.visited = [False for _ in range(self.env.n)]
        self.visited[self.initial_pos] = True
