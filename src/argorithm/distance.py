from math import sqrt 

def distance_of_point(point_1 : tuple[float, float, float], point_2 : tuple[float, float, float], Is_in_space : bool):
    """
        the point_1,2 should have 3 element in there, event it in 2D, the 3 element should be any number
        it will only caculate first 2 number which is x and y coordinated.
    """

    sum_of_square = (point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2 
    if Is_in_space: sum_of_square += (point_1[2] - point_2[2])**2 
    
    dis = sqrt(sum_of_square)
    return dis 

