from random import randint
import pygame
import time

# Настройки игры
WINDOW_SIZE = 500
TILE_SIZE = WINDOW_SIZE // 4
BACKGROUND_COLOR = (255, 255, 255)
TILE_COLOR = [(49, 134, 154), (196, 224, 235), (221, 190, 146), (213, 113, 1)]
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
def draw_zone(screen, zone, font, moves, start_time):
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, FONT_SIZE)

    for i in range(4):
        for j in range(4):
            x = j * TILE_SIZE
            y = i * TILE_SIZE
            if zone[i][j] != 0:  # Не отрисовываем пустую клетку
                pygame.draw.rect(screen, TILE_COLOR[zone[i][j] % 4], (x, y, TILE_SIZE, TILE_SIZE))
                text = font.render(str(zone[i][j]), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
                screen.blit(text, text_rect)
            pygame.draw.rect(screen, (0, 0, 0), (x, y, TILE_SIZE, TILE_SIZE), 2)
    moves_text = font.render(f"Ходы: {moves}", True, (0, 0, 0))
    screen.blit(moves_text, (10, 10))

    # Отображение времени
    elapsed_time = int(time.time() - start_time)
    time_text = font.render(f"Время: {elapsed_time} с", True, (0, 0, 0))
    screen.blit(time_text, (10, 50))

    pygame.display.update()

#Сборка всего
def main():
    while True:
        screen = game_screen()
        font = pygame.font.Font(None, FONT_SIZE)
        zone,otvet = create_zone()
        moves=0
        start_time=time.time()
        run = True
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        make_move(zone,'left')
                        moves+=1
                    elif event.key == pygame.K_UP:
                        make_move(zone,'up')
                        moves+=1
                    elif event.key == pygame.K_DOWN:
                        make_move(zone,'down')
                        moves+=1
                    elif event.key == pygame.K_RIGHT:
                        make_move(zone,'right')
                        moves+=1

            draw_zone(screen, zone, font, moves, start_time)

            if win(zone, otvet):
                elapsed_time = int(time.time() - start_time)
                print(f"Вы победили за {moves} ходов за {elapsed_time} секунд!")

                screen.fill(BACKGROUND_COLOR)
                win_text = font.render(f"Вы победили за {moves} ходов!", True, (0, 0, 0))
                time_text = font.render(f"Время: {elapsed_time} с", True, (0, 0, 0))
                replay_text = font.render("Нажмите R, чтобы сыграть ещё раз", True, (0, 0, 0))
                screen.blit(win_text, (WINDOW_SIZE // 2 - win_text.get_width() // 2, 150))
                pygame.display.update()

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                main()
main()

