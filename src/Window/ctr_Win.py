from pygame import display, event, QUIT, draw

class WINDOW():
    def __init__(self, width, hight):
        self.width = width 
        self.hight = hight 
        self.window = display.set_mode((self.width, self.hight))

    def control_event(self):
        for events in event.get():
            if events.type == QUIT:
                return False 
            
    def draw_point(self, color_point, coord_point, radius_point):
        draw.circle(self.window,
                    color_point,
                    coord_point,
                    radius_point)
        
    def update_event(self):
        display.update()