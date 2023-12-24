import pygame

# Инициализация Pygame
pygame.init()

# Определение размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Игра с перемещением игрока')

# Загрузка изображения игрока
player_image = pygame.image.load('character.png')
player_rect = player_image.get_rect()
player_rect.center = (width // 2, height // 2)

# Начальные координаты игрока
x, y = player_rect.center

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

    # Перемещение игрока
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and player_rect.right < width:
        x += speed
    if keys[pygame.K_UP] and player_rect.top > 0:
        y -= speed
    if keys[pygame.K_DOWN] and player_rect.bottom < height:
        y += speed

    # Обновление координат игрока
    player_rect.center = (x, y)

    # Заполнение экрана цветом
    screen.fill((255, 255, 255))

    # Отображение игрока на экране
    screen.blit(player_image, player_rect)

    # Обновление окна
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()