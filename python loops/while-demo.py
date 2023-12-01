# sayilar = [1,2,3,7,9,19,21]

# x = 0

# while (x< len(sayilar)):
#     print (sayilar[x])
#     x += 1

# baslangic = int(input("Başlangıç değerini giriniz: "))
# bitis = int(input("Bitiş değerini giriniz"))
# i = baslangic
# while i <= bitis:
#         if (i%2==0):
#             print (f'sayının çift hali{i}')
            
#         else:
#               print(f'sayının tek hali {i}')
#         i +=  1


# x = 100
# while x > 0:
#     x -= 1
#     print (x)


# x = 0
# sayilar = []
# while x < 5:
#     sayilar.append(int(input("BİR SAYI GİRİNİZ")))
#     x += 1
    
# print(sayilar)

urunler = []


urunsayisi = int(input("Kaç tane ürün girilecek:"))
i = 0

while (i < urunsayisi):
    name = input("Ürün ismi")
    fiyat = int(input("Ürün fiyatını giriniz"))
    i += 1
    urunler.append({"name":name,
                    "Fiyat":fiyat})


for urun in urunler:
    print (f'Ürün adı: {urun["name"]} Ürünün fiyatı: {urun["Fiyat"]}')