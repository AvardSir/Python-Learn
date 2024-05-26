import numpy as np
import matplotlib.pyplot as plt
# Параметры нормального распределения
m = 9
sigma = 2
# Генерация значений для оси x
x = np.linspace(m - 3*sigma, m + 3*sigma, 100)
# Вычисление плотности распределения для каждого значения x
y = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((x - m)/sigma)**2)
# Построение графика
plt.plot(x, y, label='Плотность нормального распределения')
plt.xlabel('x')
plt.ylabel('Плотность вероятности')
plt.title('Нормальное распределение (m=9, sigma=2)')
plt.grid(True)
plt.show()
