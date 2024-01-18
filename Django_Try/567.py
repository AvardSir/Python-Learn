import random


import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        pass
# Инициализация Pygame
pygame.init()

# Размеры окна
screen_width = 1200
screen_height = 1000
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - 50)
        self.rect.y = random.randint(0, screen_height - 50)

enemy_group = pygame.sprite.Group()

# Создание двух экземпляров врагов
enemy1 = Enemy()
enemy2 = Enemy()

enemy_group.add(enemy1, enemy2)

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



# Главный игровой цикл
running = True
while running:
    enemy_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение сосчтояния клавиш
    player_y += 0.01
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