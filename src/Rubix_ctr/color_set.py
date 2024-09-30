import const

def Get_color(point_pos : tuple[float, float, float], Block_numberess : tuple[float, float, float], block_side, block_dis, Color_blank):
    """
    Block_numberess = [block_x, block_y, block_z]
    Color_blank = None / "WHITE" / "#f000" / (0,0,0)
    """
    for k in range(3):  
        distance = (block_side * Block_numberess[k] + block_dis * (Block_numberess[k] - 1))/2
        if point_pos[k] == distance:
            return const.FACE_COLOR[k][0],k
        elif point_pos[k] == -distance:
            return const.FACE_COLOR[k][1],k + 3
    
    return Color_blank,None
