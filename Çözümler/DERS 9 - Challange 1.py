menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

print("Orijinal Menu:")

for meal in menu:
    print (meal)

print("\nGüncellenmiş Menu:")

# solution 1
for meal in menu:
    for item in meal:
        while "spam" in meal:    # spam varsa .remove(silinecek_deger) methoduyla silebiliriz
            meal.remove("spam")
    print(meal)

print("\nVersion2: ")

# solution 2
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):  # sondan index sıralar 4 elemanlıysa sıra sıra 3 2 1 0 değerleri alır
        if meal[index] == "spam":   # belli bir indexte spam varsa del fonksiyonu ile silebiliriz
            del meal[index]
    print(meal)

print("\nVersion3: ")

# solution 3
for meal in menu:
    for item in meal:
        if item != "spam":    # spam harici olan itemleri alıp yan yana yazdırıyoruz
            print(item, end=" ")     # liste görünümünü yok eder
    print()

print("\nVersion4: ")

# solution 4
for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))   # item spam değilse comma ile string .join methoduyla birleştirilir
    print(items)
    
# generator expressions
# Daha detaylı: https://dbader.org/blog/python-generator-expressions