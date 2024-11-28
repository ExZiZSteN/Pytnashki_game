from random import shuffle
import numpy as np

matrix = [x for x in range(1,16)]
shuffle(matrix)

matrix += [0]

matrix = np.reshape(matrix, (4, 4))

