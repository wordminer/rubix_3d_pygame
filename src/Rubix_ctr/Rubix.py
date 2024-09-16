from argorithm.distance import distance_in_space
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

        self.block_side = block_side
        self.block_distance = block_distance

        self.block = []
        self.Block_appear = []
        self.block_point_pos = []
        self.face_appear = []
        self.Color_face = []

        self.Axis_rotate_cube = handle_axis([0,0,0], [1,0,0], [0,1,0], [0,0,1])


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

        # for k in self.block:
        #     for face in k[1]:
        #         print(face)
        

    def set_distance_argument(self, Camera_pos : tuple[float, float, float]):
        self.Block_appear = []
        self.block_point_pos = []
        self.face_appear = []

        self.Block_appear = [
            [distance_in_space(Camera_pos, block_pos[0]), k] 
            for k, block_pos in enumerate(self.block)]
        
        self.Block_appear.sort(reverse=True)
        
        for block_pos in self.block:
            Point_coordinate =  [[distance_in_space(point_coord, Camera_pos), k] for k,point_coord in enumerate(block_pos[1])]
            Point_coordinate.sort(reverse=True)
            self.block_point_pos.append(Point_coordinate)

            #set face distance using midle point of square
            Face_dis = []
            Color = []
            for k,face_stt in enumerate(const.FACE_POS):
                Mid_pos = Midle_3D_line(block_pos[1][face_stt[1]], block_pos[1][face_stt[3]])
                Face_dis.append([distance_in_space(Camera_pos, Mid_pos),k])
                Color.append(color_set.Get_color(Mid_pos, (self.block_x, self.block_y, self.block_z), 
                                                            self.block_side,
                                                            self.block_distance))
            
            if len(self.Color_face) < len(self.block):
                self.Color_face.append(Color.copy())

            Face_dis.sort(reverse=True)
            self.face_appear.append(Face_dis.copy())

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
                                                     Scale)  ,
                              Point_argument[1])
            
            for face_point in point_pos:
                point = self.block[block_stt[1]][1][face_point[1]]

                convered_point = self.convert_point_show(point,
                                                     Window.width, Window.hight,
                                                     Camera_pos, 
                                                     Scale)            

                #print(convered_point)

                Window.draw_point(Point_argument[0], convered_point, Point_argument[1])

    def show_rubix_face(self, Window : ctr_Win.WINDOW, Camera_pos : tuple[float, float, float], Scale : list[float, float], Point_argument : list[str, int]):
        for block_stt in self.Block_appear:
            # print(block_stt)
            for face_stt in self.face_appear[block_stt[1]]:
                Face = [self.convert_point_show(self.block[block_stt[1]][1][const.FACE_POS[face_stt[1]][k]],
                                                Window.width, Window.hight,
                                                Camera_pos, 
                                                Scale) 
                        for k in range(4)]
                Window.draw_polygon(tuple(Face), self.Color_face[block_stt[1]][face_stt[1]])