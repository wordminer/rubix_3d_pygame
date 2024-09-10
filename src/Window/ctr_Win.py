from pygame import display, event, QUIT

class WINDOW():
    def __init__(self, width, hight):
        self.width = width 
        self.hight = hight 
        self.window = display.set_mode((self.width, self.hight))

    def control_event(self):
        for events in event.get():
            if events.type == QUIT:
                return False 
            
        