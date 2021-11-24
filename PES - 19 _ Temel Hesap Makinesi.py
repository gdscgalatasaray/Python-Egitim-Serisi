import math
from math import *

constants = ["pi", "e"]
non_includes = ["^", "!", "%"]
trigonometrics = ["sin", "cos", "tan", "cot", "sec", "csc"]


def is_int(x):
    if x[0] in ('-', '+'):
        return x[1:].isdigit()
    return x.isdigit()


def get_int(_boolen, x, something):
    x = input(something)
    while not is_int(x):
        x = input(something)
    return int(x)


def option1():
    print()
    print("----------Denklem Çözücü----------")
    print()
    print(f"1. Dereceden Denklem\n"
          f"2. Dereceden Denklem\n")
    a = True
    x = None
    x = get_int(a, x, "Denklemin derecesini seçiniz : ")

    if not (3 > x > 0):
        x = input("Denklemin derecesini seçiniz : ")
    else:
        if x == 1:
            print("ax+b = 0 denklemi için a'yı ve b'yi giriniz.")
            _boolen1 = True
            _boolen2 = True
            a = None
            b = None
            a = get_int(_boolen1, a, "a : ")
            b = get_int(_boolen2, b, "b : ")
            fx = -b / a
            print(f"a = {a}, b = {b} değerleri için :\nx = {fx}")
        elif x == 2:
            _boolen1 = True
            _boolen2 = True
            _boolen3 = True
            a = None
            b = None
            c = None
            a = get_int(_boolen1, a, "a : ")
            b = get_int(_boolen2, b, "b : ")
            c = get_int(_boolen2, c, "c : ")
            delta = ( b * b ) - ( 4 * a * c )
            if delta >= 0:
                fx1 = (-b - math.pow(delta, .5)) / (2 * a)
                fx2 = (-b + math.pow(delta, .5)) / (2 * a)
                print(f"a = {a}, b = {b}, c = {c} değerleri için :\nx1 = {fx1}\nx2 = {fx2}")
            else:
                print(f"a = {a}, b = {b}, c = {c} değerleri için :\nGerçek reel kök yok!")


def option2():
    print()
    print("----------Hesap Makinesi----------")
    print()
    process = str(input("Lütfen hesaplanacak değeri giriniz : "))
    left = "left"
    right = "right"

    result = None

    def find_number(x, side, _input):
        left_numbers = []
        right_numbers = []
        length_of_x = len(x)
        if side == "left":
            x_queue = _input.find(x)

            while x_queue > 0 and (_input[x_queue - 1].isdigit() or _input[x_queue - 1] == "."):
                x_queue = x_queue - 1
                left_numbers.append(_input[x_queue])

            left_numbers.reverse()

            final_string = ""
            for i in range(len(left_numbers)):
                final_string = final_string + left_numbers[i]

            return str(final_string)
        elif side == "right":
            x_queue = _input.find(x)
            while x_queue + length_of_x < len(_input) and (
                    _input[x_queue + length_of_x].isdigit() or _input[x_queue + length_of_x] == "."):
                right_numbers.append(_input[x_queue + length_of_x])
                x_queue += 1

            final_string = ""
            for i in range(len(right_numbers)):
                final_string = final_string + right_numbers[i]

            return str(final_string)

        else:
            print("WUT")

    def trigonoms(function, number):
        if function == "sin":
            return float(math.sin(number))
        elif function == "cos":
            return float(math.cos(number))
        elif function == "tan":
            return float(math.tan(number))
        elif function == "cot":
            return float(1 / math.tan(number))
        elif function == "sec":
            return float(1 / math.cos(number))
        elif function == "csc":
            return float(1 / math.sin(number))

    def reduce_layer(_process):
        global result

        _process = _process.strip()

        # ------------Constants----------- #
        if _process.count("pi") >= 1:
            _process = _process.replace("pi", f"{math.pi}", _process.count("pi"))
        if _process.count("e") >= 1:
            _process = _process.replace("e", f"{math.e}", _process.count("e"))

        # ----------Non_Includes---------- #
        while _process.count("^") > 0:
            left_number = find_number("^", left, _process)
            right_number = find_number("^", right, _process)

            if left_number.count('.') >= 1:
                left_number = float(left_number)
            else:
                left_number = int(left_number)
            if right_number.count('.') >= 1:
                right_number = float(right_number)
            else:
                right_number = int(right_number)

            _process = _process.replace(str(f'{str(left_number)}^{str(right_number)}'),
                                        str(float(math.pow(left_number, right_number))), 1)

        while _process.count("!") >= 1:
            try:
                left_number = find_number("!", left, _process)
                if left_number.count('.') >= 1:
                    left_number = float(left_number)
                else:
                    left_number = int(left_number)
                _process = _process.replace(str(f'{str(left_number)}!'),
                                            str(float(math.factorial(left_number))), 1)
            except:
                print("Faktöriyel operatörü sadece integer değer alır! ( Örnek Kullanım = 4! )")
                break

        while _process.count("%") >= 1:
            left_number = find_number("%", left, _process)
            if left_number.count('.') >= 1:
                left_number = float(left_number)
            else:
                left_number = int(left_number)
            _process = _process.replace(str(f'{str(left_number)}%'), str(float(left_number / 100)), 1)

        # ----------Trigonometrics--------- #
        for i in range(len(trigonometrics)):
            func = trigonometrics[i]
            while _process.count(f"{func}(") >= 1:
                right_number = find_number(f"{func}(", right, _process)
                if right_number.count('.') >= 1:
                    right_number = float(right_number)
                else:
                    right_number = int(right_number)
                _process = _process.replace(str(f"{func}({str(right_number)})"), str(trigonoms(func, right_number)), 1)

        return _process

    result = reduce_layer(process)

    print(eval(str(result)))


calculator = True
while calculator:
    print("1. Denklem Çözücü")
    print("2. Hesap Makinesi")
    print()
    inpt = input("Yapmak istediğiniz işlemi seçiniz : ")

    b = True
    while b:
        if inpt == "1":
            try:
                option1()
                if (inpt == "1"):
                    b = False
            except:
                None
        elif inpt == "2":
            option2()
            if (inpt == "2"):
                b = False
        else:
            inpt = input("Yapmak istediğiniz işlemi seçiniz ( Seçenekler sadece 1 ve 2'dir ) : ")
    loop = True
    while loop:
        print()
        yes_no = input("Yeni bir işlem yapmak ister misiniz ? Evet : e / Hayır : h ")
        if yes_no == "e":
            loop = False
            calculator = True
        elif yes_no == "h":
            loop = False
            calculator = False
            print("Çıkış yapıldı!")
        else:
            loop = True
