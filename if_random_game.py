y=int(input("Введите ваше число от 1 до 9: "))
def random_game(x):
    return random.randint(1,4)
if 1<=y<=4:
    print("Победа!")
else:
    print("Попробуйте еще раз!")
