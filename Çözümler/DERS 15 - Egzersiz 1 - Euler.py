"""
13195 sayısının asal bölenleri 5, 7, 13 ve 29'dur.

600851475143 sayısının en büyük asal böleni nedir?

Yapilacaklar:
-> asal mı değil mi
-> asal bölenleri bul
-> bölenlerden en büyüğünü bul
"""

def asal_mi(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x > 2:  #else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True


def asal_bolenler(x):
    asalbolenler = []
    i = 2
    while i<=x:
        if x % i == 0 and asal_mi(i):
            asalbolenler.append(i)
        i = i + 1
    return asalbolenler

def en_buyuk(liste):
    max = 0
    for i in liste:
        if i > max:
            max = i
    return max

sayi = 13195
bolenler_listesi = asal_bolenler(sayi)
print(bolenler_listesi)
print(en_buyuk(bolenler_listesi))
