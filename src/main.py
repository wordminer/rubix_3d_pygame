from Window.ctr_Win import WINDOW 
from Rubix_ctr import Rubix
import const

game_dis = WINDOW(const.WIN_WIDTH, const.WIN_HIGHT)
Cube = Rubix.Rubix_cube(3,3,1,2,0)

Cube.create_cube()
Cube.distance_argument(const.CAMERA_COORD)



while True:
    if game_dis.control_event() == False:
        exit(0)

    game_dis.window.fill("GRAY")
    
    Cube.show_rubix(game_dis, const.CAMERA_COORD, [50,50], ["RED", 5])

    game_dis.update_event()

