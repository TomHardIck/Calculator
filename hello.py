kolChis = int(input("Введите количество чисел: "))
chisla = []
for i in range(kolChis):
    chisla.append(int(input("Введите число: ")))
znak = input("Введите знак: ")
if(kolChis != 2) and (znak == '**'):
    print("Нельзя возвести в степень несколько чисел! Введите два числа.")
else:
    if(znak == '**'): print("Ответ: ", chisla[0] ** chisla[1])
    if(znak == '+'): print("Ответ: ", sum(chisla))
    if(znak == "-"):
        razn = chisla[0]
        for i in range(1, len(chisla)):
            razn -= chisla[i]
        print("Ответ: ", razn)
    if(znak == '*'):
        proizv = chisla[0]
        for i in range(1, len(chisla)):
            proizv *= chisla[i]
        print("Ответ: ", proizv)
    try:
        if(znak == '/'):
            chstn = chisla[0]
            for i in range(1, len(chisla)):
                chstn /= chisla[i]
            print("Ответ: ", chstn)
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    