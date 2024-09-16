from Window.ctr_Win import WINDOW 
from Window.ctr_mouse import Handle_mouse

from Rubix_ctr import Rubix
from Rubix_ctr import rotation_ctr

import const

game_dis = WINDOW(const.WIN_WIDTH, const.WIN_HIGHT)
Cube = Rubix.Rubix_cube(3,3,3,1,0.2)
Mouse = Handle_mouse(0.4)

Cube.create_cube()

x = 0

# Cube.set_distance_argument(const.CAMERA_COORD)
# rotation_ctr.Rotate_Cube(Cube, (45,0,0))

while True:
    
    event = game_dis.control_event()

    Mouse.Checking_mouse(game_dis.event_save)
    x_mouse, y_mouse = Mouse.Mouse_move()

    Cube.set_distance_argument(const.CAMERA_COORD)
    rotation_ctr.Rotate_Cube(Cube, (-y_mouse/50,x_mouse/50,0))

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