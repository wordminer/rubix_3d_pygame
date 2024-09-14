from math import sqrt 

def distance_in_space(point_1 : tuple[float, float, float], point_2 : tuple[float, float, float]):
    dis = sqrt(
        (point_1[0] - point_2[0])**2 +
        (point_1[1] - point_2[1])**2 +
        (point_1[2] - point_2[2])**2)
    return dis 