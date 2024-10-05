from pygame import key, display, event, QUIT, draw, KEYDOWN, K_LSHIFT, K_LCTRL
import const

def Is_in_shift(key_get):
    if key_get[K_LSHIFT]:
        return -1
    return 1

def Is_in_ctr(key_get):
    if key_get[K_LCTRL]:
        return 2
    return 1

class WINDOW():
    def __init__(self, width, hight):
        self.width = width 
        self.hight = hight 
        self.window = display.set_mode((self.width, self.hight))

    def control_event(self):
        for events in event.get():
            if events.type == QUIT:
                return False 
            
            if events.type == KEYDOWN:
                key_press = key.get_pressed()
                if events.key in const.KEY_PRESS:
                    return (const.KEY_PRESS[events.key] , Is_in_shift(key_press) * Is_in_ctr(key_press))
                
            
        
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