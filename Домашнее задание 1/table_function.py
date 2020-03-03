value = input("Введите number: ")
if value:
    number = int(value)
    if number == 3:
        print("Li")
    elif number == 17:
        print("Cl")
    elif number == 25:
        print ("Mn")
    elif number == 80:
        print ("Hg")
    else:
        print("Неизвестный элемент!")
else:
    print("Введите значение number!")
