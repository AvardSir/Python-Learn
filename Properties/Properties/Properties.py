class rabit():
    def __init__(self,color,mass):
        self.color=color
        self.mass=mass
    @property#���������, �� ����� ���� �����
    def change_mass(self):
        self.mass+=10

    @property
    def mass_allowd(self):
        return self.mass
    @mass_allowd.setter
    def mass_allowd(self,new_mass):
        self.mass+=new_mass

rab1=rabit('white',20)
print(rab1.mass_allowd)
rab1.mass_allowd(10)
print(rab1.mass_allowd)