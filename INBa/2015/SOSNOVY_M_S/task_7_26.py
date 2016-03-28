#Задача 6. Вариант 26.
#Создайте игру, в которой компьютер загадывает название одного из восьми категорий, на которые разделяются дорожные знаки в соответствии с Венской конвенцией о дорожных знаках и сигналах, а игрок должен его угадать.

#Sosnovy M.S.
#16.03.2016

import random
print("компьютер загадывает название одного из восьми категорий, на которые разделяются дорожные знаки в соответствии с Венской конвенцией о дорожных знаках и сигналах. \nУгадайте ее.")
cont = ('Предупреждающие знаки' , 'Знаки преимущественного права проезда' , 'Запрещающие и ограничивающие знаки' , 'Предписывающие знаки' , 'Знаки особых предписаний')
con = random.randint(0,4)
x=0
ball=5

while(x != 5):
    print(cont[x])
    x += 1
answer = input("\nВведите название подгруппы: ")
while(answer != cont[con]):
    print("Неверно, попробуйте ещё раз.")
    answer = input("\nВведите название подгруппы: ")
    ball -=1
if (ball < 0):
    ball = 0
print("Верно, Вы победили!\n Вы набрали: " + str(ball) + " балл(ов)")
input("\nДля выхода нажмите Enter.") 
