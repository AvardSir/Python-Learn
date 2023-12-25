import pygame
import time
pygame.init()

# Задаем размеры экрана
screen_width = 800
screen_height = 600

# Создаем экран
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Перемещение человечка")

# Загружаем изображение человечка
player_image = pygame.image.load("character.png")

# Задаем начальные координаты человечка
player_x = 100
player_y = 100

# Задаем скорость перемещения человечка
player_speed = 0.1

running = True
font = pygame.font.Font(None, 36)
start_time = time.time()
while running:
    current_time = time.time()
    elapsed_time = current_time - start_time

    # Если прошло 5 секунд, выводим сообщение
    if elapsed_time >= 2:
        # Рендерим текст
        #print('g')
        text = font.render("Привет малыш", True, 'white')
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

        # Рисуем текст на экране
        screen.blit(text, text_rect)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем состояние клавиш
    keys = pygame.key.get_pressed()

    # Перемещаем человечка влево
    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    # Перемещаем человечка вправо
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Перемещаем человечка вверх
    if keys[pygame.K_UP]:
        player_y -= player_speed

    # Перемещаем человечка вниз
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Очищаем экран
    screen.fill((0, 0, 0))

    # Отрисовываем человечка на экране
    screen.blit(player_image, (player_x, player_y))

    # Обновляем экран
    pygame.display.update()

# Завершаем Pygame
pygame.quit()