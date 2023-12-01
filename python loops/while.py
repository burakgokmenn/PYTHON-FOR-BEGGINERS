x = 1


# while x <= 100:
#     if x % 2 ==0:
#         print(f'Sayı çift{x}')
#     else:
#         print (f'Sayı tek{x}')
#     x += 1
        
name = ""

while not name.strip():
    name = input("Bir isim giriniz")
    
print (f'Merhaba {name}')