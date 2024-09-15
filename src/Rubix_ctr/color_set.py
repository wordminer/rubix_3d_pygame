import const

def Get_color(point_pos : tuple[float, float, float], Block_numberess : tuple[float, float, float], block_side, block_dis):
    """
    Block_numberess = [block_x, block_y, block_z]
    """
    for k in range(3):  
        distance = (block_side * Block_numberess[k] + block_dis * (Block_numberess[k] - 1))/2
        if point_pos[k] == distance:
            return const.FACE_COLOR[k][0]
        elif point_pos[k] == -distance:
            return const.FACE_COLOR[k][1]
    return None