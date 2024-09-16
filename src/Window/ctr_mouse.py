from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, mouse
from time import time

class Handle_mouse():    
    def __init__(self, time_check_mouse):
        self.Is_click = False        
        self.time_mouse = time_check_mouse

    def Checking_mouse(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.Is_click = True
            self.x, self.y = mouse.get_pos()
            self.time_start = time()

        elif event.type == MOUSEBUTTONUP:
            self.Is_click = False 

    def Mouse_move(self):
        if self.Is_click:
            if self.time_couting():
                self.x, self.y = mouse.get_pos()
            new_x, new_y = mouse.get_pos()

            return new_x - self.x, new_y - self.y
        return 0,0

    def time_couting(self):
        time_now = time()
        if time_now - self.time_start >= self.time_mouse:
            self.time_start = time()
            return True 
        return False