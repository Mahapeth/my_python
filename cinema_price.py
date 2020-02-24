print("Программа для подсчета стоимости билетов в кино")
film=input("Выбрать фильм: ") 
den=input("Выбрать день(сегодня,завтра): ")
seans=int(input("Выбрать время: "))
tickets=int(input("Выбрать количество билетов: "))
print("Выбрали фильм: ",film, "День: ",den, "Время: ",seans, "Количество билетов: ",tickets)
	


if film=="Паразиты" and seans==12:
    if den=="сегодня" and tickets>=20:
	    print (float(0.8*tickets*250))
    elif den=="завтра" and tickets>=20:
	    print (float(0.75*tickets*250))
    elif den=="завтра" and tickets<20:
	    print (float(0.95*tickets*250))
    else:
        print (float(tickets*250))
	
elif film=="Паразиты" and seans==16:
    if den=="сегодня" and tickets>=20:
	    print (float(0.8*tickets*350))
    elif den=="завтра" and tickets>=20:
	    print (float(0.75*tickets*350))
    elif den=="завтра" and tickets<20:
	    print (float(0.95*tickets*350))
    else:
        print (float(tickets*350))
		
elif film=="Паразиты" and seans==20:
    if den=="сегодня" and tickets>=20:
	    print (float(0.8*tickets*450))
    elif den=="завтра" and tickets>=20:
	    print (float(0.75*tickets*450))
    elif den=="завтра" and tickets<20:
	    print (float(0.95*tickets*450))
    else:
        print (float(tickets*450))

elif film=="1917" and seans==10:
    if den=="сегодня" and tickets>=20:
	    print (float(0.8*tickets*250))
    elif den=="завтра" and tickets>=20:
	    print (float(0.75*tickets*250))
    elif den=="завтра" and tickets<20:
	    print( float(0.95*tickets*250))
    else:
        print (float(tickets*250))	
elif film=="1917" and (seans==13 or seans==16):
    if den=="сегодня" and tickets>=20:
	    print (float(0.8*tickets*350))
    elif den=="завтра" and tickets>=20:
	    print (float(0.75*tickets*350))
    elif den=="завтра" and tickets<20:
	    print (float(0.95*tickets*350))
    else:
        print (float(tickets*350))
elif film=="Соник в кино" and seans==10:
    if den=="сегодня" and tickets>=20:
	    print (float(0.8*tickets*350))
    elif den=="завтра" and tickets>=20:
	    print (float(0.75*tickets*350))
    elif den=="завтра" and tickets<20:
	    print (float(0.95*tickets*350))
    else:
        print (float(tickets*350)) 
elif film=="Соник в кино" and (seans==14 or seans==18):
    if den=="сегодня" and tickets>=20:
	    print (float(0.8*tickets*450))
    elif den=="завтра" and tickets>=20:
	    print (float(0.75*tickets*450))
    elif den=="завтра" and tickets<20:
	    print (float(0.95*tickets*450))
    else:
        print (float(tickets*450))
else:
    print ("Ошибка ввода.")
