import pygame

# Инициализация Pygame
pygame.init()

# Определение размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Перемещение человечка')

# Загрузка изображения человечка
character_image = pygame.image.load('character.png')
character_rect = character_image.get_rect()
character_rect.center = (width // 2, height // 2)

# Начальные координаты человечка
x, y = character_rect.center

# Скорость перемещения
speed = 5

# Основной цикл приложения
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение состояния клавиш
    keys = pygame.key.get_pressed()
    def lol1():

        # Перемещение человечка
        if keys[pygame.K_LEFT] and character_rect.left > 0:
            x -= speed
        if keys[pygame.K_RIGHT] and character_rect.right < width:
            x += speed
        if keys[pygame.K_UP] and character_rect.top > 0:
            y -= speed
        if keys[pygame.K_DOWN] and character_rect.bottom < height:
            y += speed


    # Перемещение человечка
    if keys[pygame.K_LEFT] and character_rect.left > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and character_rect.right < width:
        x += speed
    if keys[pygame.K_UP] and character_rect.top > 0:
        y -= speed
    if keys[pygame.K_DOWN] and character_rect.bottom < height:
        y += speed

    # Обновление координат человечка
    character_rect.x = x
    character_rect.y = y

    # Обновление координат человечка
    character_rect.center = (x, y)

    # Заполнение экрана цветом
    screen.fill((255, 255, 255))

    # Отображение человечка на экране
    screen.blit(character_image, character_rect)

    # Обновление окна
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()