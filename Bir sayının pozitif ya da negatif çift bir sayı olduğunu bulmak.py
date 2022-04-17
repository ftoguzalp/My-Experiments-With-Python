sayi= float(input("Sayı giriniz:"))

if sayi>0 :
    if (sayi %2 == 0) :
        print("Girdiğiniz sayı çift pozitiftir.")
    else :
        print("Girdiğiniz sayı pozitiftir fakat tek sayıdır.")
elif sayi<=0 and (sayi %2 == 0) :
 print("Girdiğiniz sayı çift fakat pozitif değildir.")
else :
    print("Girdiğiniz sayı negatif tek sayıdır")

