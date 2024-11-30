from random import randint


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
    print(zone)
    return zone, otvet

#Проверка на ответ
def win(zone,otvet):
    if zone == otvet:
        return True


create_zone()