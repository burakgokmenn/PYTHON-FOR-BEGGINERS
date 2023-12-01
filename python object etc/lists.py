names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

names.append("Cenk")
print (names)

names.insert(0,"Sena")
print (names)
names.remove("Deniz")
print  (names)

result = "Ali" in names
print (result)

print (names[::-1])


names.sort()
print (names)

years.sort()
print (years)

print(min(years))
print(max(years))
print (years.count(1998))



str = "Cherlovet,Dacia"

result = str.split(",")

print (result)


markalar = []
marka = input("Bir Marka giriniz")
markalar.append(marka)

print (markalar)
