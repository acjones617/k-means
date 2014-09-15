import numpy as np

def normalize(matrix):
  # find average, standard deviation of each column
  # change each entry = x - mu / sigma
  normalMatrix = []
  npMatrix = np.array(matrix)
  mu = npMatrix.mean(axis=0)
  sig = npMatrix.std(axis=0)
  for sample in npMatrix:
    normalSample = []
    for i in range(len(sample)):
      normalSample.append((sample[i] - mu[i]) / sig[i])

    normalMatrix.append(normalSample)

  return normalMatrix


def reassign(original, clusters):
  finalMatrix = []
  for i in range(len(original)):
    finalMatrix.append([clusters[i][0], original[i]])

  return finalMatrix
