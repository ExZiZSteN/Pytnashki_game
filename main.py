from random import randint
import pygame

#Pygame делаю че-то
def game_screen():
    pygame.init()
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Пятнашки")



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
    i,j = find_zero(zone)

main()