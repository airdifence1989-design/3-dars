fruits = {
    "apple": 12000,
    "banana": 25000,
    "apricot": 20000,
}

bag = {}        
total = 0

while True:
    fruit = input("Введите название фрукта (apple/banana/apricot) или exit для выхода: ").lower()

    if fruit == "exit":
        break   

    if fruit not in fruits:
        print("Такого фрукта нет в списке!")
        continue

    qty = int(input("Введите количество: "))
    cost = fruits[fruit] * qty

    total += cost

    if fruit in bag:
        bag[fruit] += qty
    else:
        bag[fruit] = qty

    print(f"Стоимость сейчас: {cost} сум\n")


print("\n===== ИТОГ =====")
for f, q in bag.items():
    print(f"{f} — {q} шт — {q * fruits[f]} сум")

print("----------------------")
print("Общая стоимость:", total, "сум")


