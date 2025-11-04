
pwd = input("Введите пароль: ")

if len(pwd) > 6:
    if pwd.isdigit():
        bad = True
        for i in range(len(pwd)-1):
            if int(pwd[i+1]) - int(pwd[i]) != 1:
                bad = False
                break

        if bad:
            print("Пароль не подходит! Нельзя использовать 123456 подобное!")
        else:
            print("Пароль принят:", pwd)

    else:
        print("Пароль принят:", pwd)

else:
    print("Пароль слишком короткий!")
