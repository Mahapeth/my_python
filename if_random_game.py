y=int(input("Введите ваше число от 0 до 9: "))
def random_game(x):
    return random.randint(1,4)
if 1<=y<=4:
    print("Победа!")
elif y<1 or y>4:
    if y<1:
        print("Попробуйте еще раз! Вы загадали меньшее число.")
    elif y>4:
        print("Попробуйте еще раз!Вы загадали большее число.")
