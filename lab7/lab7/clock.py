import pygame
import time

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Название окна
pygame.display.set_caption("Mickey's Clock")

# Загрузка изображений
leftarm = pygame.image.load("lab7/images/leftarm.png")  # секундная стрелка
rightarm = pygame.image.load("lab7/images/rightarm.png")  # минутная стрелка
mainclock = pygame.transform.scale(pygame.image.load("lab7/images/clock.png"), (WIDTH, HEIGHT))

# Центр вращения (центр часов)
CENTER = (WIDTH // 2, HEIGHT // 2)

# Функция для отрисовки повернутой стрелки
def draw_rotated_arm(image, angle, pivot_offset):
    """Поворачивает изображение вокруг указанного pivot (основания стрелки)"""
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=(CENTER[0], CENTER[1] + pivot_offset))
    screen.blit(rotated_image, rotated_rect)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Получение текущего времени
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Углы поворота стрелок
    minute_angle = -(minute * 6 + second / 10)  # Минутная стрелка
    second_angle = -(second * 6)  # Секундная стрелка

    # Очистка экрана и рисование часов
    screen.blit(mainclock, (0, 0))

    # Отрисовка минутной стрелки (немного подняли pivot)
    draw_rotated_arm(rightarm, minute_angle, pivot_offset=-10)

    # Отрисовка секундной стрелки (еще чуть выше, ближе к центру)
    draw_rotated_arm(leftarm, second_angle, pivot_offset=-20)

    pygame.display.flip()
    clock.tick(60)  # Ограничение FPS

pygame.quit()