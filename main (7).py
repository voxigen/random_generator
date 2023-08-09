from random import *
special = ['_', '.', '-',]
specspecial = ['!', '@', '#' , '$', '%', '&', '*', '+', '=', ';', ':', '/', '?', '~']
Truepassword = []
Truepassword2 = []

def castom_random(special, specspecial, Truepassword, Truepassword2):
    password = int(input("Введите количество паролей для генирации:   "))
    sum_nam = int(input("Введите количество цифр в пароле:   "))
    sum_abs_upper = int(input("Введите количество заглавных букв в пароле:   "))
    sum_abs = int(input("Введите количество строчных букв в пароле:   "))
    sum_special = int(input("Введите количество спецсимволов в пароле:   "))
    sum_specspecial = int(input("Введите количество спецспецсимволов в пароле:   "))
    o = input(f'общяя длянна пароля {sum_nam + sum_abs + sum_special + sum_specspecial + sum_abs_upper}, сохранить пароли в списке? да\нет   ').lower()
    for i in range(password):
        for i2 in range(sum_abs):
            a = chr(randint(97, 122))
            Truepassword.append(a)
        for i3 in range(sum_nam):
            a = str(randint(1, 9))
            Truepassword.append(a)
        for i4 in range(sum_special):
            a = randint(0, len(special) - 1)
            Truepassword.append(special[a])
        for i5 in range(sum_specspecial):
            a = randint(0, len(specspecial) - 1)
            Truepassword.append(specspecial[a])
        for i6 in range(sum_abs_upper):
            a = chr(randint(65, 90))
            Truepassword.append(a)
        shuffle(Truepassword)
        print(*Truepassword, sep = "")
        if o == "да":
            cd = ''.join(Truepassword)
            Truepassword2.append(cd)
        Truepassword.clear()
    if o == "да":
        print(Truepassword2)
        Truepassword2.clear()
def password_random(special, specspecial, Truepassword, Truepassword2):
    password = int(input("Введите количество паролей для генирации:   "))
    sum_quantity = int(input("Введите длинну пароля:    "))
    special_sumb = input("Добавлять спецспецсимволов? да/нет:   ").lower()
    o = input("Сохранить результат в список? да/нет:    ").lower()
    for i in range(password):
        for i2 in range(sum_quantity):
            if special_sumb == "да":
                c = randint(1, 5)
            elif special_sumb == "нет":
                c = randint(1, 4)
                
            if c == 1:
                a = chr(randint(97, 122))
                Truepassword.append(a)
            if c == 2:
                a = str(randint(1, 9))
                Truepassword.append(a)
            if c == 3:
                a = randint(0, len(special) - 1)
                Truepassword.append(special[a])
            if c == 4:
                a = chr(randint(65, 90))
                Truepassword.append(a)
            if c == 5:
                a = randint(0, len(specspecial) - 1)
                Truepassword.append(specspecial[a])
        shuffle(Truepassword)
        print(*Truepassword, sep = "")
        if o == "да":
            cd = ''.join(Truepassword)
            Truepassword2.append(cd)
        Truepassword.clear()
    if o == "да":
        print(Truepassword2)
        Truepassword2.clear()
def name_random(special, specspecial, Truepassword, Truepassword2):
    name = int(input("Введите количество ников для генирации:   "))
    sum_quantity = int(input("Введите длинну ника:    "))
    sum_abs_upper = int(input("Введите количество заглавных букв в нике:   "))
    sum_special = int(input("Введите количество нижних подчеркиваний( _ ) в нике:   "))
    o = input("Сохранить результат в список? да/нет:    ").lower()
    for i in range(name):
        for i2 in range(sum_quantity - (sum_abs_upper  + sum_special)):
            a = chr(randint(97, 122))
            Truepassword.append(a)
        for i3 in range(sum_special):
            Truepassword.append("_")
        for i4 in range(sum_abs_upper):
            a = chr(randint(65, 90))
            Truepassword.append(a)
        shuffle(Truepassword)
        print(*Truepassword, sep = "")
        if o == "да":
            cd = ''.join(Truepassword)
            Truepassword2.append(cd)
        Truepassword.clear()
    if o == "да":
        print(Truepassword2)
        Truepassword2.clear()



local = input("Выберите режим генирации - пароли/ники/кастом|выйти|:   ").lower()
while local != "выйти":
    if local == "кастом":
        castom_random(special, specspecial, Truepassword, Truepassword2)
    elif local == "пароли":
        password_random(special, specspecial, Truepassword, Truepassword2)
    elif local == "ники":
        name_random(special, specspecial, Truepassword, Truepassword2)
    else:
        local = input("Выберите режим генирации - пароли/ники/кастом|выйти|:   ").lower()
        continue
    
    local2 = input("Еще раз? да/меню:   ").lower()
    if local2 == "меню":
        local = input("Выберите режим генирации - пароли/ники/кастом|выйти|:   ").lower()
        continue
    if local2 == "да":
        continue
    else:
        local2 = input("Еще раз? да/меню:   ").lower()
            
                
                
            
        
            
        
                
            
            
            
            
