from Rubix_ctr.Rubix import Rubix_cube
from argorithm.touch_polygon import point_in_polygon
from argorithm.midle_line import Midle_2D_line
from argorithm.vector_argorithm import find_vec_angle, perpendicular_vector_direc

import const
import argorithm.convert_point as convert

def check_touch_rubix(Cube : Rubix_cube, mouse_pos : tuple[float, float], Win_width, Win_hight, Camera_pos : tuple[float, float, float], Scale : tuple[int, int]):
    """
        checking touch with 6 face of cube using face present first
    """
    for face_present_key in range(3):
        Face_keys = const.FACE_POS[Cube.Face_represent_appear[face_present_key][1]]
        Face_screen_coord = [
            convert.convert_screen_point(Win_width, Win_hight, 
                                         convert.convert_3D_point(Cube.Point_corner_pos[k],
                                                                  Camera_pos),
                                         Scale[0], Scale[1])
            for k in Face_keys]
        touching = point_in_polygon(mouse_pos, Face_screen_coord, Midle_2D_line(Face_screen_coord[0], Face_screen_coord[2]))

        if touching :
            # print(const.FACE_DIRECTION_AXIS[Cube.Face_represent_appear[face_present_key][1]])
            direction_touched_key = (const.FACE_DIRECTION_AXIS[Cube.Face_represent_appear[face_present_key][1]])
            # print(Cube.Face_represent[direction_touched_key])
            for face_check in Cube.Face_represent[direction_touched_key]:
                #print(face_check)
                point_block_check = Cube.block[face_check[0]][1]
                face_stt_check = const.FACE_POS[face_check[1]]
        
                Face_screen = [
                    convert.convert_screen_point(Win_width, Win_hight, 
                                                convert.convert_3D_point(point_block_check[point_stt],
                                                                        Camera_pos),
                                                Scale[0], Scale[1])
                    for point_stt in face_stt_check]
                #print(Face_screen)
                touching_face = point_in_polygon(mouse_pos, Face_screen, 
                                                Midle_2D_line(Face_screen[0], Face_screen[2]))
                # if touching_face == False :
                #     print(Face_screen, mouse_pos)
                
                if touching_face:
                    # print(Face_screen)
                    # print(point_block_check[face_stt_check[0]])
                    # print(mouse_pos)
                    Cube.Color_face[face_check[0]][face_check[1]] = "BLACK"
                    return face_check

    
    return False

def Finding_rotate_direction(vector_touch_key : int, Cube : Rubix_cube, mouse_change_vector : tuple[float,float], Camera_pos : tuple[float, float, float]):
    """
        vector_touch_key is the key of vector rotate that have been touch and not in the rotate vector list
        so we are just check for other 2 vector, which vector is nearess with the vector of mouse, and vector rotate is the other one :))))))))
        and also, we will check for the rotate direction using other  
    """
    max_angle = 0
    vector_choose = 0
    for axis_key in range(3):

        if axis_key != vector_touch_key:
            vector_check = take_convert_vector(Cube, axis_key, Camera_pos)
            angle_vec = find_vec_angle(vector_check, mouse_change_vector)

            if angle_vec[0] >= max_angle :
                max_angle = angle_vec[0]
                vector_choose = (axis_key, vector_check)

    perpendicular_vec = perpendicular_vector_direc(vector_choose[1])
    # print(vector_choose[1])
    # print(perpendicular_vec)
    direc_rotate = find_vec_angle(perpendicular_vec, mouse_change_vector)
    return vector_choose[0], direc_rotate    
            

def take_convert_vector(Cube : Rubix_cube, Vector_key : int, Camera_pos : tuple[float, float, float]):
    Axis_Cube = Cube.Axis_rotate_blocks.Axis[Vector_key]
    Converted_vector = convert.convert_3D_point(Axis_Cube, Camera_pos)
                                                   
    return Converted_vector
    

