from pygame import display, event, QUIT, draw, KEYDOWN, K_a, K_d

class WINDOW():
    def __init__(self, width, hight):
        self.width = width 
        self.hight = hight 
        self.window = display.set_mode((self.width, self.hight))
        self.event_save = ""

    def control_event(self):
        for events in event.get():
            self.event_save = events
            if events.type == QUIT:
                return False 
            
            if events.type == KEYDOWN:
                if events.key == K_a:
                    return "a"
                if events.key == K_d:
                    return "d"
            
        
    def draw_point(self, color_point, coord_point : tuple[float, float], radius_point):
        draw.circle(self.window,
                    color_point,
                    coord_point,
                    radius_point)
        
    def draw_polygon(self, Point : tuple, color_polygon):
        if color_polygon != None:
            draw.polygon(self.window, color_polygon, Point)

    def update_event(self):
        display.update()