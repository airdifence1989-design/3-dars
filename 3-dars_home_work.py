
print("Bankomatga xush kelibsiz")
print("Bankomat 2 ta kartani qollab quvvatlaydi 1) Humo 2) UzCard")
turi = input("Qanday karta kiritasiz>> ").lower().strip()
if turi == "humo" or turi == "uzcard":
    nomer = 971234567
    karta = input("Karta raqamini kiriting: ")
    
    if len(karta) != 12:
        print("karta raqami 12 ta bolishi kerak")
    else:
        pin = input("karta parolini kiriting: ")

        if len(pin) != 4:
            print("xato parol kiritdingiz")
        else:
            print("parol togri kiritdingiz")
            if turi == "uzcard":
                hisob = 500_000
            else:
                hisob = 300_000
                
            for i in range(6):
                print("\nXizmatlar:")
                print("1) Pin kodni o`zgartirish")
                print("2) Hisobni ko`rish")
                print("3) Hisobdan pul yechish")
                print("4) SMS raqamini o`zgartirish")
                print("5) Chiqish")


                xizmatlar = int(input("Xizmat raqamini kiriting: "))

                if xizmatlar == 1:
                    eski_parol = input("Eski parolni kiriting: ")
                    
                    if eski_parol != pin:
                        print("parol xato")
                    else:
                        yangi_parol = input("yangi parol kiriting: ")
                        if len(yangi_parol) == 4:
                            print("parol ozgardi")
                            pin = yangi_parol

                elif xizmatlar == 2:
                    print(f"Xisobingizda {hisob} so'm mavjud")

                elif  xizmatlar == 3:
                    print("Yechishingiz mumkin bo'lgan summalar:")
                    print("1) 50000")
                    print("2) 200000")
                    print("3) 400000")
                    print("4) Boshqa summa")

                    tanla = input("Summalardan birini tanlang: ")

                    if tanla == "1":
                        ayir = 50000
                    elif tanla == "2":
                        ayir = 200000
                    elif tanla == "3":
                        ayir = 400000
                    elif tanla == "4":
                        kirit = input("Xoxlagan summani kiriting: ")
                        if not kirit.isdigit():
                            print("Noto`g`ri qiymat kiritildi!")
                            continue
                        ayir = int(kirit)
                    else:
                        print("Noto'g'ri tanlov qildingiz!")
                        ayir = 0
                        continue

                    if ayir > hisob:
                        print("Hisobingizda mablag' yetarli emas!")
                        continue
                    
                    tasdiq = input("Siz pul yechish operatsiyasini tasdiqlaysizmi? (1)Ha (2)Yo`q: ").lower().strip()
                    if tasdiq in ("ha", "1"):
                        hisob -= ayir
                        print(f"Operatsiya muvaffaqiyatli bajarildi!")
                        print(f"Hisobingizda {hisob:,}".replace(",", " ") + " so‘m qoldi.")
                    else:
                        print("Operatsiya bekor qilindi.")
                                                                
                elif  xizmatlar == 4:
                    if turi == "uzcard":
                         print("SMS xizmatini ulanish uchun yangi nomerini kiriting")
                         nomer = input("+998: ")
                         if not nomer.isdigit() or len(nomer) != 9:
                            print("Nomer noto`g`ri kiritilgan!")
                         else:
                            print(f"SMS raqam muvaffaqiyatli o`zgartirildi: +998{nomer}")
                     
                    else:
                        print("Ogohlantirish: Humo kartalarda nomer o`zgartirib bo`lmaydi")
                
                elif xizmatlar == 5:
                    print("Foydalanganinigiz uchun rahmat")
                    print("\n🧾 Karta ma’lumotlari:")
                    print(f"Kiritilgan karta raqami: {karta}")
                    print(f"Hozirgi PIN-kod: {pin}")
                    if turi == "uzcard":
                        print(f"SMS ulangan raqam: +998{nomer}")
                    else:
                        print("SMS xizmatiga ulangan raqam yo`q (Humo kartalarida bu xizmat mavjud emas).")
                       
                    break
                else:
                    print("Noto`g`ri xizmat raqami tanlandi.")        
                        


else:
    print("notog'ri karta turini kiritdingiz")
