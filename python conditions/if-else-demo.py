# name = input("adınızı giriniz")
# age = int(input("Yaşınızı giriniz"))
# education = input("Eğitim durumunuzu giriniz")


# if (age >= 18) and (education == "lise" or education == "lise" ):

#     print (f"Sayın {name} Tebrikler ehliyet alma hakkına sahipsiniz")

# elif (age < 18):
#     print(f"Sayın {name} Ehliyet almaya yaşınız yetmemektedir")
    
# elif(education != "lise" or education !="üniversite"):

#     print (f"Sayın {name} Ehliyet almaya eğitim durmunuz yetmemektedir")

# else:
#     print (f" Sayın {name}  Ehliyet almaya durumunuz ne eğitim açısından ne de yaş açısından yeterlidir")


# ilknot = int(input("İlk notu giriniz"))
# ikincinot = int(input("İkinci notu giriniz"))
# ucuncunot = int(input("Üçüncü notu giriniz"))

# ortalama = (ilknot+ikincinot+ucuncunot) / 3

# if (0<=ortalama<=24):
#     print ("Notunuz 0")
# elif (25<=ortalama<=44):
#     print("notunuz 1")
# elif (45<=ortalama<=54):
#     print("Notunuz 2")
# elif (55<=ortalama<=69):
#     print("Notunuz 3")
# elif (70<=ortalama<=84):
#     print("Notunuz 4")
# else: print("Notunuz 5")


import datetime

tarih = input("Aracınız hangi tarihte trafiğe çıktı (Yıl/Gün/Ay): şeklinde yazınız (Yıl/Ay/Gün):")
tarih = tarih.split("/")

print (tarih)


trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()


fark = simdi - trafigecikis
days = fark.days

if days <= 365:

    print ("Birinci servis aralığı")
elif days > 365 and  days <= 365 * 2:
    print ("2. Servis aralığı")

elif days > 365 * 2 and days <= 365*3:
    print ("Üçüncü servis aralığı")

else:
    print ("Hatalı Süre")