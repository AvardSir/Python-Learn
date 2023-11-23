"""Activate virtualenv for current interpreter:

Use exec(open(this_file).read(), {'__file__': this_file}).

This can be used when you must use an existing Python interpreter, not the virtualenv bin/python.
"""
import os
import site
import sys

try:
    abs_file = os.path.abspath(__file__)
except NameError:
    raise AssertionError("You must use exec(open(this_file).read(), {'__file__': this_file}))")

bin_dir = os.path.dirname(abs_file)
base = bin_dir[: -len("Scripts") - 1]  # strip away the bin part from the __file__, plus the path separator

# prepend bin to PATH (this file is inside the bin directory)
os.environ["PATH"] = os.pathsep.join([bin_dir] + os.environ.get("PATH", "").split(os.pathsep))
os.environ["VIRTUAL_ENV"] = base  # virtual env is right above bin directory

# add the virtual environments libraries to the host python import mechanism
prev_length = len(sys.path)
for lib in "..\Lib\site-packages".split(os.pathsep):
    path = os.path.realpath(os.path.join(bin_dir, lib))
    site.addsitedir(path.decode("utf-8") if "" else path)
sys.path[:] = sys.path[prev_length:] + sys.path[0:prev_length]

sys.real_prefix = sys.prefix
sys.prefix = base

from PIL import Image, ImageDraw

# Создание новой картинки
image = Image.new('RGB', (200, 200), color = (255, 255, 255))

# Создание объекта для рисования
draw = ImageDraw.Draw(image)

# Рисование прямоугольника
draw.rectangle([50, 50, 150, 150], fill=(0, 0, 255))

# Рисование круга
draw.ellipse([100, 100, 150, 150], fill=(255, 0, 0))

# Добавление текста
draw.text((50, 10), "Hello, World!", fill=(0, 0, 0))

# Сохранение картинки
image.save('generated_image.png')