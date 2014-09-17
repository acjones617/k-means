import numpy as np

def normalize(matrix):
  # find average, standard deviation of each column
  # change each entry = x - mu / sigma
  normal_matrix = []
  np_matrix = np.array(matrix)
  mu = np_matrix.mean(axis=0)
  sig = np_matrix.std(axis=0)
  for sample in np_matrix:
    normalSample = []
    for i in range(len(sample)):
      normalSample.append((sample[i] - mu[i]) / sig[i])

    normal_matrix.append(normalSample)

  return normal_matrix


def reassign(original, clusters):
  final_matrix = []
  for i in range(len(original)):
    final_matrix.append([clusters[i][0], original[i]])

  return final_matrix
