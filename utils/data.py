import numpy as np

class Data:
    def __init__(self, filename):
        self.filename = filename
        self.name = 'Untitled'
        self.n = 0
        self.vertices = np.empty((0, 2), dtype=np.float64)
        self.edges = None
        self.edge_id = None
        self.read_data()
        self.build_edges()
    
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
    
    def build_edges(self):
        self.edges = np.empty((self.n, self.n), dtype=np.float64)
        self.edge_id = np.empty((self.n, self.n), dtype=np.int32)
        for i in range(self.n):
            for j in range(i + 1, self.n):
                self.edges[i, j] = np.linalg.norm(self.vertices[i] - self.vertices[j])
                self.edges[j, i] = self.edges[i, j]
                self.edge_id[i, j] = self.edge_id[j, i] = i * self.n + j
