
son = int(input("Введите число: "))

qiymat = 0

for i in range(son + 1):
    if i == 0:       
        continue

    if i % 5 == 0:    
        continue

    qiymat = i**2
    print("Квадрат числа", i," = ", qiymat)

#print("Сумма всех четных чисел равна:", qiymat)