def distance(point1, point2):
    error = 0
    for ind in range(len(point1)):
        error += (point1[ind] - point2[ind])**2

    return error / len(point1)
