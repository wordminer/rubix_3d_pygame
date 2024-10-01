from pygame import mouse
from Rubix_ctr.Rubix import Rubix_cube
from Rubix_ctr.touching_check import check_touch_rubix

class Handle_mouse():    
    mouse_pressed = (0,0)
    mouse_current = (0,0)
    Is_move_cube = False
    Is_move_block = False
    Is_find_rotate_vector = False 

    Angle_rotated = 0
    Rotate_axis_key = 0

    def checking_mouse(self, Cube : Rubix_cube, Scale : tuple[int, int], Win_width, Win_hight, Camera_pos):
        mouse_click = mouse.get_pressed(3)
        if mouse_click[0]:
            touching = None
            if self.Is_move_block == False and self.Is_move_cube == False:
                touching = check_touch_rubix(Cube, mouse.get_pos(), Win_width, Win_hight, Camera_pos, Scale)

            if touching == False :
                self.Is_move_cube = True 
                self.mouse_pressed = mouse.get_pos()

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
            
    def Move_cube(self):
        if self.Is_move_cube:
            self.mouse_current = mouse.get_pos()
            mouse_change = (self.mouse_current[0] - self.mouse_pressed[0], 
                            self.mouse_current[1] - self.mouse_pressed[1])
            self.mouse_pressed = mouse.get_pos()
            return mouse_change
        return (0,0)
    
        