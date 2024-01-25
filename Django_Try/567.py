class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")

# Создаем экземпляр класса Person
person1 = Person("Иван Лашин", 21)

# Вызываем метод greet для экземпляра person1
person1.greet()
