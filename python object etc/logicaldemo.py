# number = int(input("bir sayı giriniz"))

# result = (number > 0) and (number < 100)
# print (f'girilen sayının 0-100 arasında olma durumu {result}')

# result = (number > 0) and (number %2 == 0)
# print (f'girilen sayının çift ve pozitif olma durumu {result}')


# email = input("Mail giriniz")
# password = input("Şifre giriniz")

# result = (email == "burakgokmen2014") and (password == "123abc")

# print (f'giriş durumunuz {result}')

# numberOne = int(input("Birinci sayıyı giriniz"))
# numberTwo = int(input("İkinci sayıyı giriniz"))
# numberThree = int(input("Üçüncü sayıyı giriniz"))

# sayilar = [numberOne,numberTwo,numberThree]

# sayilar.sort()
# print(f'sayiların küçükten büyüyğe sıralınşı {sayilar}')


# firstNote = int(input("İlk notu giriniz"))
# secondNote = int(input("İkinci notu giriniz"))
# thirdNote = int(input("Üçüncü notu giriniz"))

# ortalama = (firstNote+secondNote+thirdNote) / 3

# result = (ortalama >= 50)

# print (f'Geçme durumunuz{result}')

ad = input("Adınızı giriniz:")

kg = float(input("Kilonuzu giriniz"))
hg = float(input("Boyunuzu giriniz"))

indeks = (kg) /  (hg ** 2) 
zayif = (0 < indeks < 18.4 )
normal = (18.5 < indeks <24.9)
kilolu = (25 < indeks < 29.9)
obez = (30 < indeks < 34.99)


print (f'Adınız{ad} Kilonuz:{kg} Boyunuz:{hg} indeksiniz  {indeks} zayif:{zayif}')
print (f'Adınız{ad} Kilonuz:{kg} Boyunuz:{hg} indeksiniz {indeks}normal:{normal}')
print (f'Adınız{ad} Kilonuz:{kg} Boyunuz:{hg} indeksiniz {indeks}kilolu:{kilolu}')
print (f'Adınız{ad} Kilonuz:{kg} Boyunuz:{hg} indeksiniz {indeks}obez:{obez}')


