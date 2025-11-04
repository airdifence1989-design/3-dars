son = int(input("Введите число: "))

qiymat = 0

for i in range(son + 1):
    if i == 0:       
        continue

    if i % 2 != 0:    
        continue

    qiymat += i
    print(i, "+")

print("Сумма всех четных чисел равна:", qiymat)