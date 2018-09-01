#Dosya olusturmak
aDos = open("loglar.txt","w")#Var olan dosyayi acar veya olusturur ... open(r"c:\dizin\t.txt","w") olarak ta kullanilabilir
#Dosyaya yazmak
aDos.write("""
suha : 123
prof : 123""")
aDos.close()
#Dosya okumak - (r)
aDos = open("loglar.txt","r")#Kip belirtilmezse default olarak read olur
print(aDos.read())#Tum dosyayi okur
aDos.close()
aDos = open("loglar.txt","r")
print("\n",aDos.readline())#Dosyayi satir satir okur
print(aDos.readlines())#Dosyanin tamamini diziye aktarır
aDos.close()
#Dosyalari otomatik kapatma
with open("loglar.txt","r") as aDos:
    print("\n",aDos.read())
#Dosyayi ileri geri sarmak
with open("loglar.txt","r") as aDos:
    print("\n",aDos.read())
    aDos.seek(0)#Satiri basa ceker
    print("\n",aDos.read())
    print(aDos.tell())#Nere de oldugunu gosterir
#Dosyalarda degisiklik yapmak
"""Buraya kadar, Python’da bir dosyanın nasıl oluşturulacağını, boş bir dosyaya nasıl veri
girileceğini ve varolan bir dosyadan nasıl veri okunacağını öğrendik. Ama varolan ve içi
halihazırda dolu bir dosyaya nasıl veri ekleneceğini bilmiyoruz. İşte şimdi bu işlemin nasıl
yapılacağını tartışacağız.
Ancak burada önemli bir ayrıntıya dikkatinizi çekmek istiyorum. Dosyaların neresinde
değişiklik yapmak istediğiniz büyük önem taşır. Unutmayın, dosyaların başında, ortasında ve
sonunda değişiklik yapmak birbirlerinden farklı kavramlar olup, birbirinden farklı işlemlerin
uygulanmasını gerektirir.
Biz bu bölümde dosyaların baş tarafına, ortasına ve sonuna nasıl veri eklenip çıkarılacağını
ayrı ayrı tartışacağız."""
#Dosyalarin sonunda degisiklik yapmak - a
with open("loglar.txt","a") as bDos:
    bDos.write("\nenpars : 123")
with open("loglar.txt","r") as bDos:
    print(bDos.read())
with open("loglar.txt","a") as bDos:
    bDos.write("\nenparse : 123")
with open("loglar.txt","r") as bDos:
    print(bDos.read())
#Dosyalarin basinda degisiklik yapmak - r+/Yaz oku
with open("loglar.txt", "r+") as f:
    veri = f.read()
    f.seek(0) #Dosyayı başa sarıyoruz
    f.write("vegas : 123"+veri)
#Dosyalarin ortasinda degisiklik yapmak
with open("fihrist.txt", "r+") as f:
    veri = f.readlines()
    veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
    f.seek(0)
    f.writelines(veri)
#Dosyaya erisim kipleri
"""Kip
"r"
Açıklaması
Bu öntanımlı kiptir. Bu kip dosyayı okuma yetkisiyle açar. Ancak bu kipi
kullanabilmemiz için, ilgili dosyanın disk üzerinde halihazırda var olması gerekir.
Eğer bu kipte açılmak istenen dosya mevcut değilse Python bize bir hata mesajı
gösterecektir. Dediğimiz gibi, bu öntanımlı kiptir. Dolayısıyla dosyayı açarken
herhangi bir kip belirtmezsek Python dosyayı bu kipte açmak istediğimizi
varsayacaktır.
"w" Bu kip dosyayı yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya zaten disk
üzerinde varsa, Python hiçbir şey sormadan dosya içeriğini silecektir. Eğer
belirttiğiniz adda bir dosya diskte yoksa, Python o adda bir dosyayı otomatik olarak
oluşturur.
"a" Bu kip dosyayı yazma yetkisiyle açar. Eğer dosya zaten disk üzerinde mevcutsa
içeriğinde herhangi bir değişiklik yapılmaz. Bu kipte açtığınız bir dosyaya eklediğiniz
veriler varolan verilere ilave edilir. Eğer belirttiğiniz adda bir dosya yoksa Python
otomatik olarak o adda bir dosyayı sizin için oluşturacaktır.
"x" Bu kip dosyayı yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya zaten disk
üzerinde varsa, Python varolan dosyayı silmek yerine size bir hata mesajı gösterir.
Zaten bu kipin “w” kipinden farkı, varolan dosyaları silmemesidir. Eğer belirttiğiniz
adda bir dosya diskte yoksa, bu kip yardımıyla o ada sahip bir dosya
oluşturabilirsiniz.
"r+" Bu kip, bir dosyayı hem yazma hem de okuma yetkisiyle açar. Bu kipi
kullanabilmeniz için, belirttiğiniz dosyanın disk üzerinde mevcut olması gerekir.
"w+" Bu kip bir dosyayı hem yazma hem de okuma yetkisiyle açar. Eğer dosya mevcutsa
içerik silinir, eğer dosya mevcut değilse oluşturulur.
"a+" Bu kip bir dosyayı hem yazma hem de okuma yetkisiyle açar. Eğer dosya zaten disk
üzerinde mevcutsa içeriğinde herhangi bir değişiklik yapılmaz. Bu kipte açtığınız bir
dosyaya eklediğiniz veriler varolan verilere ilave edilir. Eğer belirttiğiniz adda bir
dosya yoksa Python otomatik olarak o adda bir dosyayı sizin için oluşturacaktır.
"x+" Bu kip dosyayı hem okuma hem de yazma yetkisiyle açar. Eğer belirttiğiniz adda bir
dosya zaten disk üzerinde varsa, Python varolan dosyayı silmek yerine size bir hata
mesajı gösterir. Zaten bu kipin “w+” kipinden farkı, varolan dosyaları silmemesidir.
Eğer belirttiğiniz adda bir dosya diskte yoksa, bu kip yardımıyla o ada sahip bir
dosya oluşturup bu dosyayı hem okuma hem de yazma yetkisiyle açabilirsiniz.
"rb" Bu kip, metin dosyaları ile ikili (binary ) dosyaları ayırt eden sistemlerde ikili
dosyaları okuma yetkisiyle açmak için kullanılır. “r” kipi için söylenenler bu kip için
de geçerlidir.
"wb" Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları yazma
yetkisiyle açmak için kullanılır. “w” kipi için söylenenler bu kip için de geçerlidir.
"ab" Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları yazma
yetkisiyle açmak için kullanılır. “a” kipi için söylenenler bu kip için de geçerlidir.
"xb" Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları yazma
yetkisiyle açmak için kullanılır. “x” kipi için söylenenler bu kip için de geçerlidir.
"rb+" Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları hem
okuma hem de yazma yetkisiyle açmak için kullanılır. “r+” kipi için söylenenler bu
kip için de geçerlidir.
"wb+" Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları hem
okuma hem de yazma yetkisiyle açmak için kullanılır. “w+” kipi için söylenenler bu
kip için de geçerlidir.
"ab+" Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları hem
okuma hem de yazma yetkisiyle açmak için kullanılır. “a+” kipi için söylenenler bu
kip için de geçerlidir.
"xb+" Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları hem
okuma hem de yazma yetkisiyle açmak için kullanılır. “x+” kipi için söylenenler bu kip için de geçerlidir."""