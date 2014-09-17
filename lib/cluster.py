import random
import util
from numpy import mean

def init(matrix, num_clusters):
  # select num of clusters random matrix samples
  cluster_centers = []
  samples = range(len(matrix))
  cluster_indices = []
  while len(cluster_indices) < num_clusters:
    index = random.randint(0, len(samples) - 1)
    cluster_indices.append(samples.pop(index))

  for clusterIndex in cluster_indices:
    cluster_centers.append(matrix[clusterIndex])

  return cluster_centers

def assign_points(matrix, clusters):
  clusterPoints = []
  assignedClusters = []

  for sample in matrix:
    assignedCluster = 0
    minErr = float('inf')
    for clusterInd in range(len(clusters)):
      err = util.distance(sample, clusters[clusterInd])
      if (err < minErr):
        minErr = err
        assignedCluster = clusterInd

    clusterPoints.append([assignedCluster, sample])
    assignedClusters.append(assignedCluster)

  return (clusterPoints, assignedClusters)

def reselect_centers(clusterPoints, num_clusters):
  cluster_centers = []

  for cluster in range(num_clusters):
    assigned_points = []
    for point in clusterPoints:
      if point[0] is cluster:
        assigned_points.append(point[1])

    if len(assigned_points) is not 0:
      # convert tolist() so that it can be encoded back to node correctly
      cluster_centers.append(mean(assigned_points, axis=0).tolist())

  return cluster_centers

def converged(old_clusters, clusters):
  return old_clusters == clusters
