from math import sqrt 

def distance_in_space(point_1 : tuple[float, float, float], poitn_2 : tuple[float, float, float]):
    dis = sqrt(
        (point_1[0] - poitn_2[0])**2 +
        (point_1[1] - poitn_2[1])**2 +
        (point_1[2] - poitn_2[2])**2)
    return dis 