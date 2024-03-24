


class body:#класс определяет, у него есть хп и функция вызова#класс определяет, у него есть хп и функция вызова
 hp = 30
 def __init__(self):
  pass
  #self.hp = 30

 def hand_up(self):
  print('hend up!')
  print(self.hp)

a=body()
a.hand_up()