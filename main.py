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
INFO_SIZE = 100     # Высота по y для информации

record_time = 0

#Pygame делаю че-то
def game_screen():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE,600))
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

    for i in range(4):
        for j in range(4):
            tile = zone[i][j]
            x = j * TILE_SIZE
            y = i * TILE_SIZE
            if tile != 0:  # Не рисуем пустую клетку
                pygame.draw.rect(screen, TILE_COLOR[tile % len(TILE_COLOR)],
                                 (j * TILE_SIZE, i * TILE_SIZE + INFO_SIZE, TILE_SIZE, TILE_SIZE))
                text = font.render(str(tile), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(x + TILE_SIZE // 2,
                                                  y + TILE_SIZE // 2 + INFO_SIZE))
                screen.blit(text, text_rect)

            pygame.draw.rect(screen, (0, 0, 0), (x, y + INFO_SIZE, TILE_SIZE, TILE_SIZE), 2)

    # highlight_moves(screen, zone)

    moves_text = font.render(f"Ходы: {moves}", True, (0, 0, 0))
    screen.blit(moves_text, (10, 10))

    # Отображение времени
    elapsed_time = int(time.time() - start_time)
    time_text = font.render(f"Время: {elapsed_time} с", True, (0, 0, 0))
    screen.blit(time_text, (10, 50))
    record_text = font.render(f'Рекордное время: {record_time} с',True, (0,0,0))
    screen.blit(record_text, (WINDOW_SIZE - record_text.get_width() - 10,10))
    pygame.display.update()

# # Подсветка доступных ходов
# def highlight_moves(screen, zone):
#     i, j = find_zero(zone)
#     neighbors = []  # Список соседей (доступных ходов)
#     if i > 0:  # Верхняя клетка
#         neighbors.append((i-1, j))
#     if i < 3:
#         neighbors.append((i+1, j))
#     if j > 0:  
#         neighbors.append((i, j-1))
#     if j < 3:  
#         neighbors.append((i, j+1))
#     for ni, nj in neighbors:
#         x = nj * TILE_SIZE
#         y = ni * TILE_SIZE
#         pygame.draw.rect(screen, (0, 255, 0), (x, y + INFO_SIZE, TILE_SIZE, TILE_SIZE), 5)

#Сборка всего
def main():
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
            global record_time
            elapsed_time = int(time.time() - start_time)
            print(f"Вы победили за {moves} ходов за {elapsed_time} секунд!")
            if elapsed_time < record_time or record_time == 0:
                    record_time = elapsed_time
            screen.fill(BACKGROUND_COLOR)
            win_text = font.render(f"Вы победили за {moves} ходов!", True, (0, 0, 0))
            time_text = font.render(f"Время: {elapsed_time} с", True, (0, 0, 0))
            replay_text = font.render("Нажмите R, чтобы сыграть ещё раз", True, (0, 0, 0))
            screen.blit(win_text, (WINDOW_SIZE // 2 - win_text.get_width() // 2, 150))
            screen.blit(time_text, (WINDOW_SIZE // 2 - time_text.get_width() // 2, 200))
            screen.blit(replay_text, (WINDOW_SIZE // 2 - replay_text.get_width() // 2, 250))
            pygame.display.update()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            main()
                            return
main()
