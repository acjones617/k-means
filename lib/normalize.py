from sklearn import preprocessing
import numpy as np

def normalize(matrix):
  # find average, standard deviation of each column
  # change each entry = x - mu / sigma
  # need to make at least one entry a float, or else scale will be all integers
  npMatrix = np.array(matrix)
  return preprocessing.scale(npMatrix)


