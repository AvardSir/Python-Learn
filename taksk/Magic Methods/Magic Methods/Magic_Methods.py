
class flower:
    count=0
    def __init__(self,name) -> None:
        self.name=name
        print('New flower')
        self.count+=1

    def __add__(self,other):
        self.count+=1
        print(str(self.count)+'-Flowers!!!')

Podsolnuh=flower("yelow")
Gwozdika=flower('blue')


Podsolnuh+Gwozdika
Podsolnuh+Podsolnuh

s='fff'
h='hey'
a='\n'.join([s,h,'yo'])#Check join
a=a.split('\n')#Check split
print(a)
pass