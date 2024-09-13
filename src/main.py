from Window.ctr_Win import WINDOW 
from Rubix_ctr import Rubix

game_dis = WINDOW(1000, 800)
Cube = Rubix.Rubix_cube(3,3,3,1,0)

Cube.create_cube()
Cube.distance_argument([0,0,10])



while True:
    if game_dis.control_event() == False:
        exit(0)

    game_dis.window.fill("GRAY")
    
    Cube.show_rubix(game_dis, [0,0,10], [40,40], ["RED", 5])

    game_dis.update_event()

