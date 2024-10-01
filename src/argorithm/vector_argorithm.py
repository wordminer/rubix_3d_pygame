from argorithm.distance import distance_of_point
from math import acos,pi

def find_vec_angle(vec_1 : tuple[float,float], vec_2 : tuple[float,float]):
    scalar_product = vec_1[0]*vec_2[0] + vec_1[1]*vec_2[1]
    leght_vec_1 = distance_of_point([0,0,0], vec_1, False)
    leght_vec_2 = distance_of_point([0,0,0], vec_2, False)

    if leght_vec_1 == 0 or leght_vec_2 == 0:
        return 0,1

    angle_radian = acos(scalar_product/(leght_vec_1*leght_vec_2))

    angle_vec = angle_radian * 180 / pi
    if angle_vec > 90:
        return 180 - angle_vec, -1
    return angle_vec, 1

def Is_in_good_coord(coordinate : tuple[float, float]):
    if (abs(coordinate[1]) >= 0 and abs(coordinate[0]) >= 0):
        return True

def perpendicular_vector_direc(Vector_origin : tuple[float,float]):
    """
        this is for rotate the origin vector -pi/2 radian degree
    """
    Vector_perpendicular = [Vector_origin[1], Vector_origin[0]]
    change_key = 1

    if Is_in_good_coord(Vector_perpendicular):
        change_key = 0

    Vector_perpendicular[change_key] *= -1 
    return Vector_perpendicular