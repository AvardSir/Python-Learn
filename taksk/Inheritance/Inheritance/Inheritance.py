class car():
    def __init__(self,color,speed) -> None:
        self.color=color
        self.speed=speed
    
class bus(car):
    def big_bip(self):
        print('big_bip!!!')

class sport_car(car):
    def broom(self):
        print('BROOOOOM')


Lexus=sport_car('red',130)
Lexus.broom()
School_classic_bus=bus('yelow',30)
School_classic_bus.big_bip()#classic Inheritance