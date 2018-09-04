#27 ve 31 numarali konular islenmemistir atlanmistir...
#Sozluk tanimlamak
veriler = {"pi" : 3.14,
            "e" : 2.71,
            "name" : "admin"}
print(veriler)
#Sozluk ogelerine erismek
print("Pi : ",veriler["pi"])
#Sozluklerin yapisi - Basit bir program...
db = {"users":["admin","root","suha","enpars","M E T A L L I C A"]}
a = int(input("Aramak istediginiz ismin numarasini girin (max {0}): ".format(int(len(db["users"]) -1))))
print(db["users"][a])
#Oge eklemek
db["passwords"] = ["123","321","001","0123z","2332"]
print(db)
x = input("Eklenecek kullanici (isim) : ")
y = input("Sifre : ")
db["users"] = x
db["passwords"] = y
print(db)
#Ogeler uzerinde degisiklik yapmak
db["passwords"[0]] = "asd"
print(db) 
#Sozluk uretecleri
harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
sozluk = {i: harfler.index(i) for i in harfler}#bolum ozetlendi
