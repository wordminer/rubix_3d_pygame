def Midle_3D_line(point_1 : tuple[float, float, float], point_2 : tuple[float, float, float]):
    #fiding the midle of 2 point in space
    Midle_point = [
        (point_1[k] + point_2[k])/2
        for k in range(3)]
    return Midle_point

def Midle_2D_line(point_1 : tuple[float, float], point_2 : tuple[float, float]):
    Midle_point = [
        (point_1[k] + point_2[k])/2
        for k in range(2)]
    return Midle_point