# sehirler = ["Sivas","İzmir"]
# plakalar = [58,35]


# print (sehirler[plakalar.index(58)])    


plakalar = {
"Sivas" : 58,
"İzmir" : 35,
"Ankara" : 6,
"İstanbul":34
}

print (plakalar["İzmir"])



users = {
"Burak Gökmen" : {
"Age" : 18,
"Tall" : "188CM",
"Eye Color" : "Hazel",
"Roles" : ["admin","user"]
},


"Gökçe Gökmen" : {
"Age" : 2,
"Tall" : "52cm",
"Eye Color" : "Blue",
"Roles" : ["user"]
}

}


print (users["Burak Gökmen"]["Roles"][0])