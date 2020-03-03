import random
<<<<<<< HEAD
y=int(input("Введите ваше число от 1 до 4: "))
x=random.randint(1,4)
if y==x:
=======
y=int(input("Введите ваше число от 0 до 9: "))
def random_game(x):
    return random.randint(1,4)
if 1<=y<=4:
>>>>>>> 412ae13a950fef76deacb62d6dc3f4e2fae9fbbf
    print("Победа!")
elif y<x:
    print("Попробуйте еще раз! Вы загадали меньшее число.")
elif y>x:
    print("Попробуйте еще раз!Вы загадали большее число.")
