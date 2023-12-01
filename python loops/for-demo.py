sayilar = [1,3,5,7,9,12,19,21]

# for i in sayilar:
#  if (i%3==0):
#   print (i)


toplam = 0
for sayi in sayilar:
 
  toplam += sayi
  
print ("Toplam:",toplam)


# for i in sayilar:
#   if (i%2==1):
#    print (i **2)

# sehirler = ["Kocaeli","İstanbul","Ankara","İzmir","Rize"]

# for sehir in sehirler:
#  if len(sehir) <= 5:
#   print(sehir)



urunler = [
    {"name": "Samsung S5", "Price": "3000"},
     {"name": "Samsung S6", "Price": "4000"},
     {"name": "Samsung S7", "Price": "5000"},
     {"name": "Samsung S8", "Price": "6000"},
    {"name": "Samsung S9", "Price": "7000"}
 ]

# toplam = 0
# for urun in urunler:
    

#     fiyat = int(urun["Price"])
#     toplam += fiyat

# print (toplam)


for urun in urunler:
  if (int(urun["Price"])) <= 5000:

    print (urun["name"])