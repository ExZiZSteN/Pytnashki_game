from random import randint
import pygame

#Pygame делаю че-то
def game_screen():
    pygame.init()
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Пятнашки")

#Ход
def make_move(zone,direction):
    i,j = find_zero(zone)
    if direction == 'up' and i > 0:
        zone[i][j],zone[i-1][j] = zone[i-1][j],zone[i][j]
    if direction == 'down' and i < 3:
        zone[i][l],zone[i+1][j] = zone[i+1][j],zone[i][j]
    if direction == 'left' and j > 0:
        zone[i][j],zone[i][j-1] = zone[i][j-1],zone[i][j]
    if direction == 'right' and j < 3:
        zone[i][j],zone[i][j+1] = zone[i][j+1],zone[i][j]

#Созданаие игрового поля
def create_zone():
    otvet = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,0]
        ]
    zone = otvet.copy()
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
    if zone == otvet:
        return True


#Сборка всего
def main():
    game_screen()
    zone,otvet = create_zone()
    run = True
    while run:
        pygame.time.delay(50)
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

main()