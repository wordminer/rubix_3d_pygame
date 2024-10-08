from Window.ctr_Win import WINDOW 
from Window.ctr_mouse import Handle_mouse

from Rubix_ctr import Rubix
from Rubix_ctr import rotation_ctr

import const

game_dis = WINDOW(const.WIN_WIDTH, const.WIN_HIGHT)
Cube = Rubix.Rubix_cube(const.RUBIX_BLOCK[0], const.RUBIX_BLOCK[1], const.RUBIX_BLOCK[2], const.BLOCK_LENGHT, const.BLOCK_DISTANCE)
Mouse = Handle_mouse()

Cube.create_cube()
Cube.create_face_represent(const.CAMERA_COORD)
Cube.set_color(const.COLOR_BLANK)
Cube.set_distance_argument(const.CAMERA_COORD)


while True:
    
    event = game_dis.control_event()

    mouse_pos_change = Mouse.Moving(const.CAMERA_COORD, Cube)
    check_mouse = Mouse.checking_mouse(Cube, const.WIN_SCALE, const.WIN_WIDTH, const.WIN_HIGHT, const.CAMERA_COORD)
    
    rotation_ctr.Rotate_Cube(Cube, (-mouse_pos_change[0][1], mouse_pos_change[0][0], 0))

    if mouse_pos_change[1] != None:
        rotation_ctr.Rotate_blocks(Cube, mouse_pos_change[1][0], mouse_pos_change[1][2], mouse_pos_change[1][1])

    if check_mouse != None and mouse_pos_change[1] != None:
        rotation_ctr.Rotate_blocks(Cube, mouse_pos_change[1][0], check_mouse[0], mouse_pos_change[1][1])

        for block_key in mouse_pos_change[1][1]:
            rotation_ctr.rotate_Midle_pos(Cube, mouse_pos_change[1][0], int(check_mouse[1] + check_mouse[0]),
                                        block_key, const.RUBIX_BLOCK)
    #rotation_ctr.Rotate_blocks(Cube, 0, 0.1, list_r)
    #print(Cube.Color_face)
    #touching_check.check_touch_rubix(Cube, (500,300), const.WIN_WIDTH, const.WIN_HIGHT, const.CAMERA_COORD, const.WIN_SCALE)

    # const.CAMERA_COORD = (x,0,10)
    if event == False:
        exit(0)
    elif event != None:
        rotation_ctr.Rotate_by_code(Cube, (event))

    game_dis.window.fill(const.WIN_FILL_COLOR)
    Cube.set_distance_argument(const.CAMERA_COORD)
    
    Cube.show_rubix_face(game_dis, const.CAMERA_COORD, const.WIN_SCALE)
 
    game_dis.update_event()

# Cube.set_distance_argument(const.CAMERA_COORD)
# Cube.show_rubix_face(game_dis, const.CAMERA_COORD, [50,50], ["RED", 5])

# rotation_ctr.Rotate_Cube(Cube, (1,0,0))
# Cube.set_distance_argument(const.CAMERA_COORD)

# Cube.show_rubix_face(game_dis, const.CAMERA_COORD, [50,50], ["RED", 5])