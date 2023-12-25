
[app]
#target = android 
version = 1.0.0

package.name = com.planet.py


# Имя вашего приложения
title = planet.py

# Путь до файла main.py (исходного файла .py)
source.dir = C:\github\C#\Learn\Python-Learn\Django_Try\planet.py

# Имя файла main.py
source.include_exts = planet.py

# Имя главного файла (который будет запущен)
source.main.filename = planet.py

# Другие файлы и папки, которые необходимо включить
#source.include_patterns = README.md

# Используйте это, если ваше приложение использует другие библиотеки
requirements = python3,pygame,math

# Целевая архитектура Android-устройств
android.arch = armeabi-v7a

# Другие параметры, такие как иконка приложения и версия