
class Rubix_cube():
    def __init__(self, block_x, block_y, block_z, block_side, block_distance):
        self.block_x = block_x
        self.block_y = block_y
        self.block_z = block_z

        self.block_side = block_side
        self.block_distance = block_distance

    def create_cube(self):
        #Center = [0,0,0]
        Start_point = [-(self.block_side + self.block_distance)*(block-1)/2 
                       for block in [self.block_x, self.block_y, self.block_z]]
        
        self.block = [
            [Start_point[k] + (self.block_side + self.block_distance) * Pos for k, Pos in enumerate([x,y,z]) ] 

            for x in range(self.block_x) 
                for y in range(self.block_y)
                     for z in range(self.block_z)
        ]


test = Rubix_cube(2, 2, 2, 1, 1)
test.create_cube()

