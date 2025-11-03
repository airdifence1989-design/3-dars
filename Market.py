
products = {
    "1":("Milk", 12000),
    "2":("Bread", 5000),
    "3":("Meat", 120000),
    "4":("Fish",80000),
    "5":("Oil", 22000),
    "6":("Banana", 25000),
    "7":("Apple", 18000)
}
print(" \n Welcome to the Korzinka market! \n")
print(" You can choose products: ")
for key,(name,price) in products.items():
    print(f'{key}.{name}-{price} sum')
cart=[]
for i in range(3):
    choice=input(f"\n Choose the product №{i+1}: ")
    if choice not in products:
        print("Sorry there is not product you choose!")
        continue
    kol=int(input(f"how much/many '{products[choice][0]}' you want to buy? ")) 
    cart.append((products[choice][0], products[choice][1], kol))
total=sum(price*qty for _, price, qty in cart)
discount=0
if total > 100000:
    discount = total*0.1
    total-=discount

print("\n Your check ")
for name, price, check in cart:
    print(f'{name}x{check}={price*check} sum')

print(f"\n Your discount = :{int(discount)} sum")
print(f"Total cost to pay: {int(total)} sum ")
payment_type=input("\n Choose variant to pay (cash / card):").lower()
if payment_type=="card":
    card_type=input("Inter your card type (uzcard / humo):").lower()
    card_number=input("Enter your card number: ")
    if len(card_number)!=12:
        print("Your card number is incorrect! ")
        exit()

    password=input("Enter your card password: ")
    if card_type=="uzcard":
            balance=300000
    elif card_type=="humo":
            balance=200000
    else:
            print("Card type is incorrect! Try again! ")
            exit()
    if total>balance:
            print("You don't have enough money on your card!")
    else:
            balance-=total
            print(f'Your payment was successful! \n Your balance is: {int(balance)} sum')
elif payment_type=="cash":
    print("Payment with cash was succesful! ")

else:
    print("Incorrect payment type!")
print("\n Purchase succesful completed! ")
for name, price, qty in cart:
    print(f'{name} - {qty} kg(l), price: {price*qty} sum')

print(f"\n Discount = : {int(discount)} sum")
print(f"Total pay = : {int(total)} sum")
print(f"\n Thank you for your purchase! we are waiting for you again!")



