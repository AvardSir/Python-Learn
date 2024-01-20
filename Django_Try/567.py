import tkinter as tk

def display_text():
    label.config(text="Привет, мир!")
    button.config(text="Привет, мир!")
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
