from Window.ctr_Win import WINDOW 
from Rubix_ctr import Rubix
from Rubix_ctr import rotation_ctr

import const

game_dis = WINDOW(const.WIN_WIDTH, const.WIN_HIGHT)
Cube = Rubix.Rubix_cube(3,3,3,1,0.2)

Cube.create_cube()

x = 0

while True:
    
    event = game_dis.control_event()
    
    rotation_ctr.Rotate_Cube(Cube, (1,0,0))

    Cube.set_distance_argument(const.CAMERA_COORD)

    

    const.CAMERA_COORD = (x,0,10)
    if event == False:
        exit(0)
    elif event == "a":
        x += 0.05
    elif event == "d":
        x -= 0.05

    game_dis.window.fill("GRAY")
    
    # Cube.show_rubix_point(game_dis, const.CAMERA_COORD, [50,50], ["RED", 5])
    Cube.show_rubix_face(game_dis, const.CAMERA_COORD, [50,50], ["RED", 5])

    game_dis.update_event()

# Cube.set_distance_argument(const.CAMERA_COORD)
# Cube.show_rubix_face(game_dis, const.CAMERA_COORD, [50,50], ["RED", 5])

# rotation_ctr.Rotate_Cube(Cube, (1,0,0))
# Cube.set_distance_argument(const.CAMERA_COORD)

# print("A")

# Cube.show_rubix_face(game_dis, const.CAMERA_COORD, [50,50], ["RED", 5])
