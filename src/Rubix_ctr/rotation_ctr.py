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

            Cube.Axis_rotate_cube.rotate_axis(Rotation_angel[0], Cube.Axis_rotate_cube.Axis[0])

        Cube.Axis_rotate_blocks.rotate_axis(Rotation_angel[k_rotate], Cube.Axis_rotate_cube.Axis[k_rotate])

        
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

    if number_of_round == 0:
        return 

    if number_of_round < 0:
        handle_rotate = -1
    
    Pos_pressed = Cube.block[block_key][2].copy()
    key_pos_change = const.ROTATION_MIDLE_POS_KEY[Vector_rotate_key]

    # print(Pos_pressed, "--->", end = "")

    if number_of_round == 2:
        Cube.block[block_key][2][key_pos_change[handle_rotate]] = Block_numberes[key_pos_change[handle_rotate]] - Pos_pressed[key_pos_change[handle_rotate]] - 1
        Cube.block[block_key][2][key_pos_change[handle_rotate + 1]] = Block_numberes[key_pos_change[handle_rotate + 1]] - Pos_pressed[key_pos_change[handle_rotate + 1]] - 1 
    else:
        Cube.block[block_key][2][key_pos_change[handle_rotate + 1]] = Block_numberes[key_pos_change[handle_rotate]] - Pos_pressed[key_pos_change[handle_rotate]] - 1
        Cube.block[block_key][2][key_pos_change[handle_rotate]] = Pos_pressed[key_pos_change[handle_rotate + 1]]

    # print(Cube.block[block_key][2])
    rotate_face_axis(Cube, Vector_rotate_key, block_key, number_of_round)

def finding_rotate_block(Cube : rubix.Rubix_cube, Vector_rotate_key : int, pos_rotation : int):
    """
        pos rotation mean the x or y or z pos in Cube.block[k][2] 
    """
    List_block_rotate = []

    if Vector_rotate_key >= 3: Vector_rotate_key -= 3

    for k,block in enumerate(Cube.block):
        if block[2][Vector_rotate_key] == pos_rotation:
            List_block_rotate.append(k)

    return List_block_rotate

def rotate_face_axis(Cube : rubix.Rubix_cube, Vector_rotate_key : int, block_stt, round_of_rotate : int):
    if round_of_rotate == 0:
        return   
    
    Add_list = []
    Del_list = []

    for face_stt, face in enumerate(Cube.Face_represent):
        #print(face_stt)
        if face_stt == Vector_rotate_key or face_stt == Vector_rotate_key + 3:
            continue
        Vector_key = face_stt % 3
        #print(face_stt, Vector_key)

        for stt,block in enumerate(face):
            if block[0] == block_stt:
                if round_of_rotate == 2:
                    new_asix_key = face_stt - 3
                    
                else :
                    for k in range(3):
                        if k != Vector_key and k != Vector_rotate_key:
                            new_asix_key = k
                            break
                            

                    if Cube.block[block_stt][2][new_asix_key] == 0:
                        new_asix_key += 3

                #print(face_stt, new_asix_key, block[0])
                
                Add_list.append([new_asix_key, block.copy()])
                Del_list.append([face_stt, stt])
                break

    for k in range(len(Add_list)):
        Cube.Face_represent[Add_list[k][0]].append(Add_list[k][1])
        del(Cube.Face_represent[Del_list[k][0]][Del_list[k][1]])
                 

        