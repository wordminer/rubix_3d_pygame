from .. import const

class Rubix_cube():
    def __init__(self, block_x, block_y, block_z, block_side, block_distance):
        self.block_x = block_x
        self.block_y = block_y
        self.block_z = block_z

        self.block_side = block_side
        self.block_distance = block_distance

    def create_cube(self):
        print(const.win_hight)


new = Rubix_cube(1, 1, 1, 1, 1)
new.create_cube()