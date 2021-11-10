import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


class Data:
    def __init__(self, filename):
        self.filename = filename
        self.name = 'Untitled'
        self.n = 0
        self.vertices = np.empty((0, 2), dtype=np.float64)
        self.edges = None
        self.edge_id = None
        print('Reading data...')
        self.read_data()
        print('Data read')
        print("Building edges...")
        self.build_edges()
        print('Edges built')
    
    def read_data(self):
        coord_read_started = False
        with open(self.filename, 'r') as f:
            for line in f:
                if line.startswith('NAME'):
                    self.name = line.split()[-1]
                elif line.startswith('DIMENSION'):
                    self.n = int(line.split()[-1])
                elif line.startswith('EDGE_WEIGHT_TYPE'):
                    if line.split()[-1] != 'EUC_2D':
                        raise Exception('Only EUC_2D is supported')
                elif line.startswith('NODE_COORD_SECTION'):
                    coord_read_started = True
                elif coord_read_started:
                    if line.startswith('EOF'):
                        break
                    else:
                        coords = [float(coord) for coord in line.split()[1:]]
                        self.vertices = np.concatenate([self.vertices, np.array(coords).reshape(1, 2)])
        
        self.vertices = np.unique(self.vertices, axis=0)
        self.n = self.vertices.shape[0]

    def build_edges(self):
        self.edges = np.eye(self.n)
        vals = np.expand_dims(self.vertices, axis=1) - np.expand_dims(self.vertices, axis=0)
        self.edges = np.linalg.norm(vals, axis=-1)
        self.edges += np.eye(self.n)

def plot_length(path_length_history):
    plt.plot(path_length_history)
    plt.xlabel('Iteration')
    plt.ylabel('Path length')
    plt.show()

def plot_path(path, vertices):
    path_cycle = path + [path[0]]
    plt.plot(vertices[path_cycle, 0], vertices[path_cycle, 1], '-o')
    plt.show()

def save_path(filename, path):
    with open('res.txt', 'w+') as f:
        for city in path:
            f.write(str(city + 1) + '\n')