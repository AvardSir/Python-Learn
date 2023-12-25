import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Игра с перемещением человечка")

# Загрузка изображения человечка
player_image = pygame.image.load("character.png")
player_rect = player_image.get_rect()
player_rect.center = (width // 2, height // 2)

# Скорость перемещения
speed = 5

# Основной цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение состояния клавиш
    keys = pygame.key.get_pressed()

    # Перемещение человечка
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN]:
        player_rect.y += speed

    # Заполнение экрана цвет