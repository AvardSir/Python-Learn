import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
screen_width = 1200
screen_height = 1000

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Простой 2D платформер")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Позиция и скорость игрока
player_x = 50
player_y = 50
player_speed = 0.1
print('yi')
# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print('yofk')

    # Получение состояния клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Отрисовка игровых объектов
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, 50, 50))

    # Обновление экрана
    pygame.display.flip()

# Выход из игры
pygame.quit()