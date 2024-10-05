from argorithm.distance import distance_of_point
from argorithm.convert_point import convert_3D_point, convert_screen_point
from argorithm.midle_line import Midle_3D_line
from argorithm.handle_rotate import handle_axis
from Window import ctr_Win
from Rubix_ctr import color_set

import const

class Rubix_cube():
    def __init__(self, block_x, block_y, block_z, block_side, block_distance):
        self.block_x = block_x
        self.block_y = block_y
        self.block_z = block_z

        self.Max_hight = 0

        self.block_side = block_side
        self.block_distance = block_distance

        self.block = []
        self.Block_appear = []
        self.block_point_pos = []
        self.face_appear = []
        self.Color_face = []
        self.Point_corner_pos = []
        self.Face_represent = [[] for k in range(6)]
        self.Face_represent_appear = []

        self.Axis_rotate_cube = handle_axis([0,0,0], [1,0,0], [0,1,0], [0,0,1])
        self.Axis_rotate_blocks = handle_axis([0,0,0], [1,0,0], [0,1,0], [0,0,1])

    def create_face_represent(self, Camera_pos : tuple[float, float, float]):
        self.Point_corner_pos = [
            [x_pos * ((self.block_side) * self.block_x /2  + self.block_distance * (self.block_x /2 - 1)  ),
             y_pos * ((self.block_side) * self.block_y /2  + self.block_distance * (self.block_y /2 - 1)  ),
             z_pos * ((self.block_side) * self.block_z /2  + self.block_distance * (self.block_z /2 - 1)  )]
             for x_pos in [-1,1]
             for y_pos in [-1,1]
             for z_pos in [-1,1]
        ]
        #self.Max_hight = distance_of_point(self.Point_corner_pos[0], [0,0,0])
        #print(self.Point_corner_pos)
        
    def create_cube(self):
        #Center = [0,0,0]
        Start_point = [-(self.block_side + self.block_distance)*(block-1)/2 
                       for block in [self.block_x, self.block_y, self.block_z]]
        
        self.block = [
            [ [Start_point[k] + (self.block_side + self.block_distance) * Pos for k, Pos in enumerate([x,y,z])], [], [x,y,z] ]
            for x in range(self.block_x) 
            for y in range(self.block_y)
            for z in range(self.block_z)
        ]

        # start to put coord in to each block

        for k in range(len(self.block)):
            self.block[k][1] +=  [
                [self.block[k][0][i] + self.block_side/2 * vec for i,vec in enumerate([vec_x, vec_y, vec_z])]
                for vec_x in [-1,1]
                for vec_y in [-1,1]
                for vec_z in [-1,1]
            ] 

        # for k in self.block:
        #     for face in k[1]:
        #         print(face)

    def set_color(self, Color_blank):
        """Color_blank = None / "WHITE" / "#f000" / (0,0,0)"""
        Del_block = []

        for k,block_pos in enumerate(self.block):
            #set face distance using midle point of square
            Color = []
            for face_key,face_stt in enumerate(const.FACE_POS):
                Mid_pos = Midle_3D_line(block_pos[1][face_stt[1]], block_pos[1][face_stt[3]])
                face_color, Axis_face_key = color_set.Get_color(Mid_pos, (self.block_x, self.block_y, self.block_z), 
                                                            self.block_side,
                                                            self.block_distance, Color_blank)
                Color.append(face_color)

                if Axis_face_key != None:
                    # print(Axis_face_key)
                    # print(k - len(Del_block), face_key)
                    # print("------------------")
                    self.Face_represent[Axis_face_key].append([k - len(Del_block), face_key])
            
            if all(color_face == None for color_face in Color):
                Del_block.append(k)
                continue

            self.Color_face.append(Color.copy())

        for block_d in Del_block:
            del(self.block[block_d])
            for k in range(len(Del_block)):
                Del_block[k] -= 1

        # print(self.Face_represent)

    def set_distance_argument(self, Camera_pos : tuple[float, float, float]):
        self.Block_appear = []
        self.block_point_pos = []
        self.face_appear = []
        self.Face_represent_appear = []
        """
            set distance for block appear
        """
        self.Block_appear = [
            [distance_of_point(Camera_pos, block_pos[0], True), k] 
            for k, block_pos in enumerate(self.block)]
        
        self.Block_appear.sort(reverse=True)
        """
            set distance for each face in block
        """
        for block_pos in self.block:
            Point_coordinate =  [[distance_of_point(point_coord, Camera_pos, True), k] for k,point_coord in enumerate(block_pos[1])]
            Point_coordinate.sort(reverse=True)
            self.block_point_pos.append(Point_coordinate)

            #set face distance using midle point of square
            Face_dis = []
            for k,face_stt in enumerate(const.FACE_POS):
                Mid_pos = Midle_3D_line(block_pos[1][face_stt[1]], block_pos[1][face_stt[3]])
                Face_dis.append([distance_of_point(Camera_pos, Mid_pos, True),k])
            
            Face_dis.sort(reverse=True)
            self.face_appear.append(Face_dis.copy())
        """
            set distance for 4 corner of cube
        """
        for key, face_stt in enumerate(const.FACE_POS):
            Midpoint = Midle_3D_line(self.Point_corner_pos[face_stt[0]], self.Point_corner_pos[face_stt[2]])
            #print(self.Point_corner_pos)
            self.Face_represent_appear.append([distance_of_point(Midpoint, Camera_pos, True), key, Midpoint])

        self.Face_represent_appear.sort()
        # print(self.Face_represent_appear)
        # print("//////////////////////")


        # print(self.face_appear)

    def convert_point_show(self, point : tuple[float, float, float], width : int, hight : int, Camera_pos : tuple[float, float, float], Scale : list[float, float]):
        convered_point = convert_screen_point(
                    width, hight,
                    convert_3D_point(point, Camera_pos),
                    Scale[0], Scale[1])
        
        return convered_point


    def show_rubix_point(self, Window : ctr_Win.WINDOW, Camera_pos : tuple[float, float, float], Scale : list[float, float], Point_argument : list[str, int]):
        
        for block_stt in self.Block_appear:
            point_pos = self.block_point_pos[block_stt[1]]
            Window.draw_point(Point_argument[0], self.convert_point_show(self.block[block_stt[1]][0],
                                                     Window.width, Window.hight,
                                                     Camera_pos, 
                                                     Scale),
                              Point_argument[1])
            
            for face_point in point_pos:
                point = self.block[block_stt[1]][1][face_point[1]]

                convered_point = self.convert_point_show(point,
                                                     Window.width, Window.hight,
                                                     Camera_pos, 
                                                     Scale)            

                #print(convered_point)

                Window.draw_point(Point_argument[0], convered_point, Point_argument[1])

    def show_rubix_face(self, Window : ctr_Win.WINDOW, Camera_pos : tuple[float, float, float], Scale : list[float, float]):
        for block_stt in self.Block_appear:
            # print(block_stt)
            for face_stt in self.face_appear[block_stt[1]]:
                Face = [self.convert_point_show(self.block[block_stt[1]][1][const.FACE_POS[face_stt[1]][k]],
                                                Window.width, Window.hight,
                                                Camera_pos, 
                                                Scale) 
                        for k in range(4)]
                Window.draw_polygon(tuple(Face), self.Color_face[block_stt[1]][face_stt[1]])