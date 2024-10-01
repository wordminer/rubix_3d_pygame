import Rubix_ctr.Rubix as rubix
from argorithm.handle_rotate import rotate_point
from argorithm.congruance_find import congruance_of_p
import const

def Rotate_Cube(Cube : rubix.Rubix_cube, Rotation_angel : tuple[float, float, float]):
    for k_rotate in range(3):
        if Rotation_angel[k_rotate] == 0:
            continue
                
        if k_rotate == 0:
            if abs(Cube.Axis_rotate_cube.Rotated_angle[0] + Rotation_angel[0]) > 90:
                continue

            Cube.Axis_rotate_cube.rotate_axis(Rotation_angel[0], 0)
        
        for block_stt, block in enumerate(Cube.block):
            for k, point in enumerate(block[1]):
                Cube.block[block_stt][1][k] = rotate_point([0,0,0], 
                                                        Cube.Axis_rotate_cube.Axis[k_rotate],
                                                        point, 
                                                        Rotation_angel[k_rotate])
            
            Cube.block[block_stt][0] = rotate_point([0,0,0], 
                                                    Cube.Axis_rotate_cube.Axis[k_rotate],
                                                    block[0], 
                                                    Rotation_angel[k_rotate])
            
        for corner_key, corner_pos in enumerate(Cube.Point_corner_pos):
            Cube.Point_corner_pos[corner_key] = rotate_point([0,0,0], 
                                                            Cube.Axis_rotate_cube.Axis[k_rotate],
                                                            corner_pos, 
                                                            Rotation_angel[k_rotate])
        
        Cube.Axis_rotate_blocks.rotate_axis(Rotation_angel[k_rotate], k_rotate)


def Rotate_blocks(Cube : rubix.Rubix_cube, Vector_rotate_key : int, rotate_angle : float, block_rotate_key : list):
    for block_stt in block_rotate_key:
        block = Cube.block[block_stt]
        for k, point in enumerate(block[1]):
            Cube.block[block_stt][1][k] = rotate_point([0,0,0], 
                                                    Cube.Axis_rotate_blocks.Axis[Vector_rotate_key],
                                                    point, 
                                                    rotate_angle)
        
        Cube.block[block_stt][0] = rotate_point([0,0,0], 
                                                Cube.Axis_rotate_blocks.Axis[Vector_rotate_key],
                                                block[0], 
                                                rotate_angle)
        
def rotate_Midle_pos(Cube : rubix.Rubix_cube, Vector_rotate_key : int, rotate_angle : int, block_key : int, Block_numberes : tuple[int, int, int]):
    """
        This will rotate the Cube.block[k][2] pos 
        which help the program know exacly where the block are when they find the block to rotate
        and thi type of pos will just call Rotation_pos

        Note: just use this when rotate_angle is 90, 180, 270,... or negative
    """
    if rotate_angle % 90 != 0:
        return 
    
    number_of_round = congruance_of_p(4, rotate_angle/90)
    handle_rotate = 0

    if number_of_round < 0:
        handle_rotate = -1
    
    Pos_pressed = Cube.block[block_key][2].copy()
    key_pos_change = const.ROTATION_MIDLE_POS_KEY[Vector_rotate_key]

    # print(Pos_pressed, "--->", end = "")

    if number_of_round == 2:
        Cube.block[block_key][2][key_pos_change[0]] = Block_numberes[key_pos_change[-1]] - Pos_pressed[key_pos_change[-1]] - 1
        Cube.block[block_key][2][key_pos_change[1]] = Block_numberes[key_pos_change[0]] - Pos_pressed[key_pos_change[0]] - 1
        return 

    Cube.block[block_key][2][key_pos_change[handle_rotate + 1]] = Block_numberes[key_pos_change[handle_rotate]] - Pos_pressed[key_pos_change[handle_rotate]] - 1
    Cube.block[block_key][2][key_pos_change[handle_rotate]] = Pos_pressed[key_pos_change[handle_rotate + 1]]

    # print(Cube.block[block_key][2])

def finding_rotate_block(Cube : rubix.Rubix_cube, Vector_rotate_key : int, pos_rotation : int):
    """
        pos rotation mean the x or y or z pos in Cube.block[k][2] 
    """
    List_block_rotate = []

    for k,block in enumerate(Cube.block):
        if block[2][Vector_rotate_key] == pos_rotation:
            List_block_rotate.append(k)

    return List_block_rotate

