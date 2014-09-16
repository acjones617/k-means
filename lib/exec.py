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
normalMatrix = n.normalize(matrix)

# 2. randomly pick cluster center points
clusterCenters = c.init(normalMatrix, options['clusters'])

# 3. assign points to a cluster

# 4. re-pick cluster center points

# 5. repeat steps 3 and 4
for i in range(options['iterations']):
    clusterPoints = c.assignPoints(normalMatrix, clusterCenters)
    clusterCenters = c.reselectCenters(clusterPoints, options['clusters'])

# final assignment of points
clusterPoints = c.assignPoints(normalMatrix, clusterCenters)

# 6. assign clusters to original data
finalMatrix = n.reassign(matrix, clusterPoints)

# 7. send back to node - need to convert cluster centers to list first
print j.encode({
    'finalMatrix'   : finalMatrix,
    'clusterCenters': clusterCenters
})

