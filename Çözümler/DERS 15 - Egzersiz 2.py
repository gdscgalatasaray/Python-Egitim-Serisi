"""
dik kenarları a,b ve hipotenüsü c olan ve
a<=100, b<=100 şartlarını karşılayan pisagor üçgenlerini hesaplayın.
a^2 + b^2 = c^2
"""

def pisagor():
    pisagor_sayilari = []
    for a in range(1,101):
        for b in range(1,101):
            c = (a ** 2 + b ** 2)**0.5
            if c == int(c):
                pisagor_sayilari.append((a,b,int(c)))
    return pisagor_sayilari

print(pisagor())