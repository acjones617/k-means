import random
import util
from numpy import mean

def init(matrix, numClusters):
  # select num of clusters random matrix samples
  clusterCenters = []
  samples = range(len(matrix))
  clusterIndices = []
  while len(clusterIndices) < numClusters:
    index = random.randint(0, len(samples) - 1)
    clusterIndices.append(samples.pop(index))

  for clusterIndex in clusterIndices:
    clusterCenters.append(matrix[clusterIndex])

  return clusterCenters

def assignPoints(matrix, clusters):
  clusterPoints = []

  for sample in matrix:
    assignedCluster = 0
    minErr = float('inf')
    for clusterInd in range(len(clusters)):
      err = util.distance(sample, clusters[clusterInd])
      if (err < minErr):
        minErr = err
        assignedCluster = clusterInd

    clusterPoints.append([assignedCluster, sample])

  return clusterPoints

def reselectCenters(clusterPoints, numClusters):
  clusterCenters = []

  for cluster in range(numClusters):
    assignedPoints = []
    for point in clusterPoints:
      if point[0] is cluster:
        assignedPoints.append(point[1])

    if len(assignedPoints) is not 0:
      # conver tolist() so that it can be encoded back to node correctly
      clusterCenters.append(mean(assignedPoints, axis=0).tolist())

  return clusterCenters
