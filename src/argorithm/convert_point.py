def convert_3D_point(point : tuple[float, float, float], Camera : tuple[float, float, float]):
    # print(point)
    # print(Camera)
    VTCP = [point[0] - Camera[0], point[1] - Camera[1], point[2] - Camera[2]]
    HS = Camera[2] / (Camera[2] - point[2])
    x = HS * VTCP[0] + Camera[0]
    y = HS * VTCP[1] + Camera[1]
    
    return ((x - Camera[0]),(y - Camera[1]))

def convert_screen_point(dis_width, dis_hight, point_real : tuple[float, float, float], scale_x, scale_y):
    point_scale = [point_real[0] * scale_x, point_real[1] * scale_y]
    point_screen = [point_scale[0] + dis_width/2, point_scale[1] + dis_hight/2]

    return point_screen
