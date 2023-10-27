
class fox:
    def __init__(self,color,speed):
        self.color=color
        self.speed=speed
        self._attributes=[self.color,self.speed]
    def set_color(self,color):
        self.color=color
        self._attributes[0]=self.color
    def set_speed(self,speed):
        self.speed=speed
        self._attributes[1]=self.speed

    def get_color(self):
        return self._attributes[0]
    def get_speed(self):
        return self._attributes[1]
    def __mistery_fox(self):#Double underline for top secret
        return ("secret DEF found")

mini_fox=fox('yelow',120)
mini_fox.set_color('red_orange')
print(mini_fox.get_color())#гетеры сетеры
print(mini_fox._attributes)#скрытие условно

print(mini_fox._fox__mistery_fox())#_fox после Ќјзвание скрытойфункции===>вызов еЄ