from pygame import mouse
from Rubix_ctr.Rubix import Rubix_cube
from Rubix_ctr.touching_check import check_touch_rubix, Finding_rotate_direction
from Rubix_ctr.rotation_ctr import finding_rotate_block
import argorithm.vector_argorithm as vector
from argorithm.distance import distance_of_point

class Handle_mouse():    
    mouse_pressed = (0,0)
    mouse_current = (0,0)
    Is_move_cube = False
    Is_move_block = False
    Is_find_rotate_vector = False 

    Angle_rotated = 0
    Rotate_axis_key = 0
    Block_move_list = []
    perpencular_vec = []
    touching = None

    def checking_mouse(self, Cube : Rubix_cube, Scale : tuple[int, int], Win_width, Win_hight, Camera_pos):
        mouse_click = mouse.get_pressed(3)
        if mouse_click[0]:
            touching = None
            if self.Is_move_block == False and self.Is_move_cube == False:
                touching = check_touch_rubix(Cube, mouse.get_pos(), Win_width, Win_hight, Camera_pos, Scale)

            if touching == False :
                self.Is_move_cube = True 
                self.mouse_pressed = mouse.get_pos()

            elif touching != False and touching != None:
                self.Is_move_block = True 
                self.Is_find_rotate_vector = True
                self.mouse_pressed = mouse.get_pos()
                self.touching = touching
                print(touching)

            # if check_touch_rubix(Cube, mouse_click):
            #     self.Is_move_block = True 
            #     self.Is_find_rotate_vector = True 
            # else:
            #     self.Is_move_cube = True 
            #     self.mouse_pressed = mouse.get_pos() 
        else:
            self.Is_move_cube = False
            self.Is_move_block = False
            self.Angle_rotated = 0
            
    def take_mouse_change(self):
        self.mouse_current = mouse.get_pos()
        mouse_change = (self.mouse_current[0] - self.mouse_pressed[0], 
                        self.mouse_current[1] - self.mouse_pressed[1])
        self.mouse_pressed = mouse.get_pos()
        # print(mouse_change)
        return mouse_change
    
    def take_angle_rotate(self, Mouse_change : tuple[float,float]):
        angle = vector.find_vec_angle(Mouse_change, self.perpencular_vec)
        cosin_bet_vec = vector.cos(vector.radians(angle[0]))
        lenght_move_vec = distance_of_point(Mouse_change, [0,0,0], False) * cosin_bet_vec

        return (lenght_move_vec * angle[1])

        
    
    def Moving(self, Camera_pos : tuple[float,float,float], Cube : Rubix_cube):
        Moving_thing = [(0,0), None]
        Mouse_change = self.take_mouse_change()

        if self.Is_move_cube:
            Moving_thing[0] = Mouse_change

        if self.Is_move_block == True and self.Is_find_rotate_vector == False :
            angle_rotate = self.take_angle_rotate(Mouse_change)
            Moving_thing[1] = [self.Rotate_axis_key, self.Block_move_list, angle_rotate]
            self.Angle_rotated += angle_rotate

        if self.Is_move_block == True and self.Is_find_rotate_vector == True:
            if abs(Mouse_change[0]) < 3 and abs(Mouse_change[1]) < 3:
                return Moving_thing
            
            self.Rotate_axis_key, self.perpencular_vec = Finding_rotate_direction(self.touching[1], Cube, Mouse_change, Camera_pos)
            self.Block_move_list = finding_rotate_block(Cube, self.Rotate_axis_key,
                                                        Cube.block[self.touching[0]][2][self.Rotate_axis_key])
            self.Is_find_rotate_vector = False

        return Moving_thing
        