import random
x=random.randint(1,4)
while True:
    y=int(input("Введите ваше число от 1 до 4: "))
    if y==x:
        print("Победа!")
        break
    elif y<x:
        print("Попробуйте еще раз! Вы загадали меньшее число.")
    elif y>x:
        print("Попробуйте еще раз!Вы загадали большее число.")

