
# 2017-2018 Guz Donemi
# Bilgisayar Muhendisligine Giris
# Finalde Sorulan Programlar

# 2. Soru
def spam(number) :
    if (number[0] % 2) == 0 :
        number[0] = number[0] // 4
        print(number[0])
    
def bacon(number) :
    if (number[0] % 2) != 0 :
        number[0] = 5 * number[0] + 1
        print(number[0])
    
number = [30]
while number[0] > 1 :
    spam(number)
    bacon(number)

