import random
y=int(input("Введите ваше число от 1 до 4: "))
x=random.randint(1,4)
if y==x:
    print("Победа!")
elif y<x:
    print("Попробуйте еще раз! Вы загадали меньшее число.")
elif y>x:
    print("Попробуйте еще раз!Вы загадали большее число.")
