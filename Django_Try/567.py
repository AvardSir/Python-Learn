print(3*(10**3)/2.8*(10**1))
class Person:


    def __init__(self, name, age):
        self.g = '*'
        self.name = name
        self.age = age

    def greet(self):

        print(self.g*10)

# Создаем экземпляр класса Person
person1 = Person("Иван Лашин", 21)
person2 = Person("Иван Лашин", 21)
# Вызываем метод greet для экземпляра person1
person1.greet()


class Body:

    def __init__(self, uron, bronya,max_hp):
        self.uron = uron
        self.bronya = bronya
        self.max_hp = max_hp
        self.hp=max_hp

    def status(self):
        #'*'
        self.status_hp=int((self.hp/self.max_hp)*10)
        print(int(self.hp/self.max_hp)*10)
        print(self.hp)
        print(self.status_hp*'*')
        print(self.status_hp * '*')
        print(self.status_hp * '*')
        print(self.status_hp * '*')
        print(self.status_hp * '*')
    def udar(self,kovo_bit):ч
        kovo_bit.hp-=(self.uron)*(self.bronya/10)kovo_bit.hp-=(self.uron)*(self.bronya/10)kovo_bit.hp-=(self.uron)*(self.bronya/10)kovo_bit.hp-=(self.uron)*(self.bronya/10)kovo_bit.hp-=(self.uron)*(self.bronya/10)kovo_bit.hp-=(self.uron)*(self.bronya/10)
kovo_bit.hp-=(self.uron)*(self.bronya/10)
kovo_bit.hp-=(self.uron)*(self.bronya/10)kovo_bit.hp-=(self.uron)*(self.bronya/10)kovo_bit.hp-=(self.uron)*(self.bronya/10)



kovo_bit.hp -= (self.uron) * (self.bronya / 10)
kovo_bit.hp-=(self.uron)*(self.bronya/10)
        kovo_bit.hp -= (self.uron) * (self.bronya / 10)
        kovo_bit.hp -= (self.uron) * (self.bronya / 10)kovo_bit.hp -= (self.uron) * (self.bronya / 10)
        kovo_bit.hp -= (self.uron) * (self.bronya / 10) kovo_bit.hp -= (self.uron) * (self.bronya / 10)
        #'*'
Hero=Body(10,10,100)
Evil_guy=Body(10,10,100)

Hero.udar(Evil_guy)
for i in range(5):
    Hero.udar(Evil_guy)
Evil_guy.status()

