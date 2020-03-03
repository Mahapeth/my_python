import random
list = ['самовар', 'весна', 'лето']
word = random.choice(list)
letter = random.choice(word)
index=word.find(letter)
word1=word[:index] + "?" +word[index +1:]
print (word1)
v=str(input("Введите букву: "))
if v==letter:
    print ("Победа!")
else:
    print ("Ува! Попробуте в другой раз.")
print("Слово: ",word )
