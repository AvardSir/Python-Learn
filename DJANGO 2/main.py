import pandas as pd
import pymysql.cursors
import matplotlib.pyplot as plt
# Подключение к базе данных:
connection = pymysql.connect(host = '127.0.0.1',user = 'root', password = '', db ='mydb',charset ='utf8mb4',cursorclass = pymysql.cursors.DictCursor)
def get_data(request):

  with connection.cursor() as cursor:
    sql = request
    cursor.execute(sql)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)

    connection.close()
  return df


def users_weight():
  df=get_data("SELECT * FROM анкета ")
  plt.xlabel('Пол')
  plt.ylabel('Вес')
  plt.title('Распределение веса Мужчин и женщин')
  plt.bar(df['Пол'],df['ВЕС']) # гистограмма
  #plt.show()

def users_weight2():
  import matplotlib.pyplot as plt
  df=get_data("SELECT * FROM анкета ")

  plt.xlabel('123')
  plt.ylabel('ВОАОАОА')
  plt.title('Популярность 5 групп')


  ax= df['Группы'].plot(kind='hist', bins=5)
  ax.set_ylabel('Частота')
  ax.set_xlabel('Группы')

  # Отображаем график
  plt.show()

def users_weight2():
  import matplotlib.pyplot as plt
  df=get_data("SELECT * FROM анкета ")

  plt.xlabel('123')
  plt.ylabel('ВОАОАОА')
  plt.title('Популярность 5 групп')


  ax= df['Группы'].plot(kind='hist', bins=5)
  ax.set_ylabel('Частота')
  ax.set_xlabel('Группы')

  # Отображаем график
  plt.show()
def krug():
  import pandas as pd
  import matplotlib.pyplot as plt
  df = get_data("SELECT * FROM анкета ")

  import pandas as pd
  import matplotlib.pyplot as plt
  value_counts = df['Пол'].value_counts('м')

  data = {'value': [value_counts['м'], value_counts['ж']]}
  labels = ['мужской', 'женский']
  s = pd.Series(data['value'], index=labels, name='')

  # Строим круговую диаграмму
  s.plot(kind='pie', autopct='%1.1f%%')

  # Отображаем диаграмму
  plt.axis('equal')  # Задаем равный масштаб
  plt.title('соотношения полов в анкетах')
  plt.show()


krug()
#users_weight2()
#users_weight2()
#users_weight()
import random


# with connection.cursor() as cursor:
#
#   for idАнкета in range(8,15):
#     random_number = random.randint(1, 5)
#     if random.randint(1, 2)==2:
#       pol='м'
#     else:
#       pol = 'ж'
#     print('g')
#     #cursor.execute("INSERT INTO `mydb`. `анкета`(`idАнкета`, `ФИО`, `ВЕС`, `Пол`, `Группы`, `Сообщения`, `Страница с контентом`, `Список друзей`) "
#      #              "VALUES(idАнкета, str(idАнкета), str(random.randint(1, 5)*20), pol, random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5));")
#
#
#     random_number = random.randint(1, 5)
#     #cursor.execute("INSERT INTO `mydb`. `анкета` (`idАнкета`, `ФИО`, `ВЕС`, `Пол`, `Группы`, `Сообщения`, `Страница с контентом`, `Список друзей`) VALUES (%s, %s,%s,%s,%s,%s,%s,%s, )",
#      #                                             (idАнкета, str(idАнкета), str(random.randint(1, 5)*20), pol, random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)))
#
#     #connection.close()
#
#
#   #SELECT * FROM mydb.контент;    #Ctrl + Shift + _Ctrl + Shift + _
#   #INSERT INTO `mydb`. `анкета`(`idАнкета`, `ФИО`, `ВЕС`, `Пол`, `Группы`, `Сообщения`, `Страница с контентом`, `Список друзей`) VALUES(FLOOR(RAND() * 125) + 1, FLOOR(RAND() * 125) + 1, FLOOR(RAND() * 125) + 1, 'м', FLOOR(RAND() * 5) + 1, FLOOR(RAND() * 5) + 1, FLOOR(RAND() * 5) + 1, FLOOR(RAND() * 5) + 1);