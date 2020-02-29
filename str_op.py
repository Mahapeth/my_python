s = "У лукоморья 123 дуб зеленый 456"
symb="я"
for i in range(len(s)):
    if s[i]==symb:
        print("Индекс буквы Я: ",i)
s1=sum(1 for i in str(s) if i=="у")
print("Буква У встречается ",s1," раз")
if str(s).isalpha()==False:
    print (str(s).upper())
if len(str(s))>4:
    print(str(s).lower())
s1=str(s).replace(s[0],"O")
print(s1)

    
