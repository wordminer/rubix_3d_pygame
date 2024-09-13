from argorithm.distance import distance_in_space

class Rubix_cube():
    def __init__(self, block_x, block_y, block_z, block_side, block_distance):
        self.block_x = block_x
        self.block_y = block_y
        self.block_z = block_z

        self.block_side = block_side
        self.block_distance = block_distance

        self.block = []
        self.block_appear = []
        self.block_face_coord =[]

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

    def distance_argument(self, Camera_pos : tuple):
        self.block_appear = []
        self.block_face_coord = []

        self.block_appear = [
            [distance_in_space(Camera_pos, block_pos[0]), k] 
            for k, block_pos in enumerate(self.block)]
        
        self.block_appear.sort(reverse=True)
        
        for block_pos in self.block:
            Point_coordinate =  [[distance_in_space(point_coord, Camera_pos), k] for k,point_coord in enumerate(block_pos[1])]
            Point_coordinate.sort(reverse=True)
            self.block_face_coord.append(Point_coordinate)

test = Rubix_cube(2, 2, 2, 1, 0)
test.create_cube()
test.distance_argument((0,0,3))

