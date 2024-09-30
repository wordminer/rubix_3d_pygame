from Window.ctr_Win import WINDOW 
from Window.ctr_mouse import Handle_mouse

from Rubix_ctr import Rubix
from Rubix_ctr import rotation_ctr

import const

game_dis = WINDOW(const.WIN_WIDTH, const.WIN_HIGHT)
Cube = Rubix.Rubix_cube(1,1,1,1,0)
Mouse = Handle_mouse()

Cube.create_cube()
Cube.create_face_represent()
Cube.set_color("#606060")

x = 0

# Cube.set_distance_argument(const.CAMERA_COORD)
# rotation_ctr.Rotate_Cube(Cube, (-45,-45,0))

# list_r = rotation_ctr.finding_rotate_block(Cube, 0, 0)
# rotation_ctr.Rotate_blocks(Cube, 0, 90, list_r)
# for block_r in list_r:
#     rotation_ctr.rotate_Midle_pos(Cube, 0, 90, block_r, (3,3,3))



while True:
    
    event = game_dis.control_event()

    mouse_pos_change = Mouse.Move_cube()
    Mouse.checking_mouse(Cube, [1,1])
    

    Cube.set_distance_argument(const.CAMERA_COORD)
    rotation_ctr.Rotate_Cube(Cube, (-mouse_pos_change[1], mouse_pos_change[0], 0))
    #rotation_ctr.Rotate_blocks(Cube, 0, 0.1, list_r)
    #print(Cube.Color_face)

    const.CAMERA_COORD = (x,0,10)
    if event == False:
        exit(0)
    elif event == "a":
        x += 0.05
    elif event == "d":
        x -= 0.05

    game_dis.window.fill("GRAY")
    
    Cube.show_rubix_face(game_dis, const.CAMERA_COORD, [50,50], ["RED", 5])

    #Cube.show_rubix_point(game_dis, const.CAMERA_COORD, [50,50], ["RED", 5])
    
    game_dis.update_event()

# Cube.set_distance_argument(const.CAMERA_COORD)
# Cube.show_rubix_face(game_dis, const.CAMERA_COORD, [50,50], ["RED", 5])

# rotation_ctr.Rotate_Cube(Cube, (1,0,0))
# Cube.set_distance_argument(const.CAMERA_COORD)

# Cube.show_rubix_face(game_dis, const.CAMERA_COORD, [50,50], ["RED", 5])