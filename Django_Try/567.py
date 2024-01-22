import tkinter as tk

def display_text():
    i=0
    if i ==0:

        label.config(text="Привет, мир!")
    button.config(text="Привет, мир!")
    button.config(text="Привет, ы!")
    button.config(text="Привет, ы!")
    button.config(text="Привет, ы!")

# Создаем главное окно
root = tk.Tk()
root.title("Приложение с кнопкой")

# Создаем метку для отображения текста
label = tk.Label(root, text="")
label.pack(pady=20)

# Создаем кнопку
button = tk.Button(root, text="Нажми меня", command=display_text)
button.pack()

# Запускаем основной цикл обработки событий
root.mainloop()
