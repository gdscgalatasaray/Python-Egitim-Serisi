current_choice = "-"  # herhangi bir değer olabilirdi, while'a girebilmesi için "0"dan farklı olmalı
computer_parts = []   # liste tanımladık, eklenen parçaları buraya koyacağız

while current_choice != '0':
    if current_choice in "123456":  # current_choice "123456" stringi içinde mi diye bakıyor
        print("Adding {}".format(current_choice))   # içindeyse bunu yazdırır
        if current_choice == '1':  # bu sefer daha spesifik arıyoruz sonrasında ona göre listeye o parçayı ekliyoruz
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("mouse mat")
        elif current_choice == '6':
            computer_parts.append("hdmi cable")
    else: 
    # current_choice "123456" stringi içinde değilse menuyu tekrar oynatır(Program başında current_choice "-" olduğundan ilk burayı oynatacak)
        print("Please add options from the list below")
        print("1: computer")
        print("2: monitor")
        print("3: keyboard")
        print("4: mouse")
        print("5: mouse mat")
        print("6: hdmi cable")
        print("0: to finish")
    current_choice = input()  # inputu üstteki menüden sonra alıyoruz

print(computer_parts) # current_choice "0" ise while döngüsü kırılır ve liste yazdırılır