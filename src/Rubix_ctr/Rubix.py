
class Rubix_cube():
    def __init__(self, block_x, block_y, block_z, block_side, block_distance):
        self.block_x = block_x
        self.block_y = block_y
        self.block_z = block_z

        self.block_side = block_side
        self.block_distance = block_distance
        self.block = [1]

    def create_cube(self):
        #Center = [0,0,0]
        Start_point = [-(self.block_side + self.block_distance)*(block-1)/2 
                       for block in [self.block_x, self.block_y, self.block_z]]
        
        self.block = [
            [ [Start_point[k] + (self.block_side + self.block_distance) * Pos for k, Pos in enumerate([x,y,z])] ]

            for x in range(self.block_x) 
                for y in range(self.block_y)
                     for z in range(self.block_z)
        ]

        # start to put coord in to each block

        for k in range(len(self.block)):
            self.block[k] +=[ [
                [self.block[k][-1][i] + self.block_side/2 * vec for i,vec in enumerate([vec_x, vec_y, vec_z])]
                for vec_x in [-1,1]
                    for vec_y in [-1,1]
                        for vec_z in [-1,1]
            ] ]

        

test = Rubix_cube(2, 2, 2, 1, 0)
test.create_cube()

