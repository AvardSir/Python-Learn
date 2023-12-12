def lol1():

    import math
    import random
    import numpy

    import matplotlib.pyplot as plt
    def telecom1():

        R=10
        print(random.random() * R * R)

    R=10
    print(R**2)

#python#
import tkinter as tk
from tkinter import messagebox

# Функция, которая будет вызываться при нажатии на кнопку
def show_message():
    messagebox.showinfo("Сообщение", "Привет, тебе!")

# Создание основного окна
window = tk.Tk()

# Создание кнопки
button = tk.Button(window, text="Нажми меня", command=show_message)

# Размещение кнопки на окне
button.pack()

# Запуск основного цикла обработки событий
window.mainloop()
