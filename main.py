from random import randint
import pygame

# Настройки игры
WINDOW_SIZE = 500
TILE_SIZE = WINDOW_SIZE // 4
BACKGROUND_COLOR = (255, 255, 255)
TILE_COLOR = (0, 150, 136)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 40

#Pygame делаю че-то
def game_screen():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE,WINDOW_SIZE))
    pygame.display.set_caption("Пятнашки")
    return screen

#Ход
def make_move(zone,direction):
    i,j = find_zero(zone)
    if direction == 'up' and i > 0:
        zone[i][j],zone[i-1][j] = zone[i-1][j],zone[i][j]
    if direction == 'down' and i < 3:
        zone[i][j],zone[i+1][j] = zone[i+1][j],zone[i][j]
    if direction == 'left' and j > 0:
        zone[i][j],zone[i][j-1] = zone[i][j-1],zone[i][j]
    if direction == 'right' and j < 3:
        zone[i][j],zone[i][j+1] = zone[i][j+1],zone[i][j]

#Создание игрового поля
def create_zone():
    otvet = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,0]
        ]
    zone = [row[:] for row in otvet]
    for i in range(4):
        for j in range(4):
            x1,y1 = i,j
            x2, y2 = randint(0,3), randint(0,3)
            zone[x1][y1],zone[x2][y2] = zone[x2][y2], zone[x1][y1]
    return zone, otvet

#Нахождение пустой клетки
def find_zero(zone):
    for i in range(4):
        for j in range(4):
            if zone[i][j] == 0:
                return i,j

#Проверка на ответ
def win(zone,otvet):
    return zone == otvet

# Отрисовка игрового поля
def draw_zone(screen, zone):
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, FONT_SIZE)

    for i in range(4):
        for j in range(4):
            x = j * TILE_SIZE
            y = i * TILE_SIZE
            if zone[i][j] != 0:  # Не отрисовываем пустую клетку
                pygame.draw.rect(screen, TILE_COLOR, (x, y, TILE_SIZE, TILE_SIZE))
                text = font.render(str(zone[i][j]), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
                screen.blit(text, text_rect)

    pygame.display.update()

#Сборка всего
def main():
    screen = game_screen()
    zone,otvet = create_zone()
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            make_move(zone,'left')
        if keys[pygame.K_UP]:
            make_move(zone,'up')
        if keys[pygame.K_DOWN]:
            make_move(zone,'down')
        if keys[pygame.K_RIGHT]:
            make_move(zone,'right')

        draw_zone(screen, zone)

        if win(zone, otvet):
            print("Вы победили!")
            run = False

    pygame.quit()

main()