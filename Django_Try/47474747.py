def get_array_name(array):
    # Перебираем глобальные переменные и находим ту, которая ссылается на тот же объект, что и array
    for name, value in globals().items():
        if value is array:
            return name
    return None

# Пример использования функции
my_array = [1, 2, 3, 4, 5]
array_name = get_array_name(my_array)
print(f"Название массива:{array_name}" )
