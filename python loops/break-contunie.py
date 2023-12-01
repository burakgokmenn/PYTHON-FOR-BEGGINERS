# name = 'Burak'
# for letter in name:
#     print (letter)
#     if letter == 'a':
#         break

# name = "Burak"

# for i in name:
#     if i == "r":
#         continue
#     print(i)


# x = 0

# while x < 10:
#     x += 1
#     if x == 5:
#         continue
#     print (x)

x  = 0
toplam = 0

while x <= 7:
    x += 1
    if x %2 == 1:
        continue
    toplam += x


print(toplam)