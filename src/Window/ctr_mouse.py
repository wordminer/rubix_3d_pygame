from pygame import mouse
from argorithm import touch_polygon
from Rubix_ctr.Rubix import Rubix_cube

def checking_touch(Cube : Rubix_cube):
    pass

class Handle_mouse():    
    mouse_pressed = (0,0)
    mouse_current = (0,0)
    Is_move_cube = False

    def checking_mouse(self):
        mouse_click = mouse.get_pressed(3)
        if mouse_click[0]:
            self.Is_move_cube = True 
            self.mouse_pressed = mouse.get_pos()
        else:
            self.Is_move_cube = False
            
    def Move_cube(self):
        if self.Is_move_cube:
            self.mouse_current = mouse.get_pos()
            mouse_change = (self.mouse_current[0] - self.mouse_pressed[0], 
                            self.mouse_current[1] - self.mouse_pressed[1])
            self.mouse_pressed = mouse.get_pos()
            return mouse_change
        return (0,0)