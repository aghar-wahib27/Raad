from Vital import singleton

@singleton
class EventHandler:
    def __init__(self):

        self.events={
            k:[] for k in 
                ['mouse_down','mouse_released','key_down',
                 'right_pressed','right_released','left_pressed','left_released',
                 'up_pressed','up_released','down_pressed','down_released',
                 'a','w','d','s',
                 'left','right','up','down',
                 'mouse_pos','esc','space']
                }

        self.actions={k:0 for k in self.events}

    def append(self,groups:list,ent:any):
        for gr in groups:
            self.events[gr].append(ent)

    def update_event(self,event='',val=1):
        for ent in self.events[event]:
            ent.events[event]=val

Handler=EventHandler()

class EE:
    def __init__(self,events:list):
        self.events={k:0 if k!='mouse_pos' else (0,0)   for k in events}

        Handler.append(groups=[evt for evt in self.events],ent=self)



