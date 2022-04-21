class TRoad:
    def __init__(self, lendth_user, width_user):
        if lendth_user>0:
            self.lendth=lendth_user
        else:
            self.lendth=0
        if width_user>0:
            self.width=width_user
        else:
            self.width=0
class TCar:
    def __init__(self, road_user, p_user, v_user):
        self.road=road_user
        self.p=p_user
        self.v=v_user
        self.x=0
    def move(self):
        self.x+=self.v
        if self.x>self.road.lendth:
