from Rubix_ctr.Rubix import Rubix_cube
from argorithm.touch_polygon import point_in_polygon
from argorithm.midle_line import Midle_2D_line
from argorithm.vector_argorithm import find_vec_angle

import const
import argorithm.convert_point as convert

def check_touch_rubix(Cube : Rubix_cube, mouse_pos : tuple[float, float], Win_width, Win_hight, Camera_pos : tuple[float, float, float], Scale : tuple[int, int]):
    """
        checking touch with 6 face of cube using face present first
    """
    for face_present_key in range(3):
        Face_keys = const.FACE_POS[Cube.Face_represent_appear[face_present_key][1]]
        Face_screen_coord = [
            convert.convert_screen_point(const.WIN_WIDTH, const.WIN_HIGHT, 
                                         convert.convert_3D_point(Cube.Point_corner_pos[k],
                                                                  const.CAMERA_COORD),
                                         Scale[0], Scale[1])
            for k in Face_keys]
        touching = point_in_polygon(mouse_pos, Face_screen_coord, Midle_2D_line(Face_screen_coord[0], Face_screen_coord[2]))
        if touching :
            print(const.FACE_DIRECTION_AXIS[Cube.Face_represent_appear[face_present_key][1]])
            return
    
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

            

def take_convert_vector(Cube : Rubix_cube, Vector_key : int, Camera_pos : tuple[float, float, float]):
    Axis_Cube = Cube.Axis_rotate_blocks.Axis[Vector_key]
    Converted_vector = convert.convert_3D_point(Axis_Cube, Camera_pos)
                                                   
    return Converted_vector
    

