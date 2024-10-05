from pygame import K_a, K_u, K_d, K_r, K_l, K_f, K_b

WIN_WIDTH = 1000
WIN_HIGHT = 600

RUBIX_BLOCK = (3,3,3)
BLOCK_LENGHT = 1
BLOCK_DISTANCE = 0.3

COLOR_BLANK = "BLACK"

CAMERA_COORD = (0,0,100)
WIN_SCALE = [80,80]
WIN_FILL_COLOR = "GRAY"

FACE_POS = (
    (0,1,3,2),
    (4,5,7,6),
    (2,6,7,3),
    (0,4,5,1),
    (1,3,7,5),
    (2,6,4,0)
)

FACE_DIRECTION_AXIS = [3,0,1,4,2,5]

FACE_COLOR = [
    ["YELLOW", "RED"],
    ["BLUE", "GREEN"],
    ["WHITE", "PURPLE"]
]

ROTATION_MIDLE_POS_KEY = [[2,1], [0,2], [1,0]]

KEY_PRESS = {
    K_u : (1,0),
    K_d : (0,1),
    K_r : (0,2),
    K_l : (1,3),
    K_f : 4,
    K_b : 5
}

