ogrenciler = {
 120 : {
 "ad" : "Ali",
 "soyad": "Yılmaz",
 "telefon": "532 532 00 00 00"
 },

 125 : {
 "ad" : "Can",
 "soyad": "Korkmaz",
 "telefon" : "0545 545 00 00"
 },


 128 : {
 "ad" : "Volkan",
 "soyad" : "Konak",
 "telefon" : "0552 552 00 00"

}

}


number = int(input("Öğrenci Numarasını giriniz"))

print (f'Aradığınız {number} nolu öğrencinin Adı Soyadı {ogrenciler[number]["ad"] + " " + ogrenciler[number]["soyad"]+ "Telefonu ise " + ogrenciler[number]["telefon"]}')




# ogrenciler = {}


# number = input("Öğrenci Numarasını giriniz")
# name = input("Öğrenci adını giriniz")
# surname = input("Öğrenci soyadını giriniz")
# phone = input("Öğrenci telefon numarsaını giriniz")

# ogrenciler[number] = {
# "ad" : name,
# "soyad" : surname,
# "phone" : phone
# }

# print (ogrenciler)