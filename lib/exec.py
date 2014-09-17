import normalize as n
import cluster as c

import jsonpickle as j
import argparse
import ast

parser = argparse.ArgumentParser()
parser.add_argument('matrix')
parser.add_argument('options')
args   = parser.parse_args()

matrix = ast.literal_eval(args.matrix)
options = ast.literal_eval(args.options)

# steps:
# 1. normalize data
# 2. randomly pick center points
# 3. assign points to a cluster
# 4. re-pick cluster center points
# 5. repeat
# 6. assign clusters to original data
# 7. send back to node

# steps:
# 1. normalize data
normal_matrix = n.normalize(matrix)

# 2. randomly pick cluster center points
cluster_centers = c.init(normal_matrix, options['clusters'])

# 3. assign points to a cluster

# 4. re-pick cluster center points

# 5. repeat steps 3 and 4
clusters = []
has_converged = False

for i in range(options['iterations']):
    old_clusters = clusters
    cluster_points, clusters = c.assign_points(normal_matrix, cluster_centers)
    if c.converged(old_clusters, clusters):
        has_converged = True
        break
    cluster_centers = c.reselect_centers(cluster_points, options['clusters'])

# final assignment of points if never converged
if (not has_converged):
    cluster_points, clusters = c.assign_points(normal_matrix, cluster_centers)

# 6. assign clusters to original data
final_matrix = n.reassign(matrix, cluster_points)

# 7. send back to node - need to convert cluster centers to list first
print j.encode({
    'finalMatrix'   : final_matrix,
    'clusterCenters': cluster_centers
})

