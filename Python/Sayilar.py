#Sayilarin Metotlari
#Tam Sayilarin Metotlari
#bit_lenght - Verinin bellekte kac bitlik yer kapladigini verir
x = 4
t = 0
y = 12+4j
z = 4.5
l = [12,321,11,321,312313,123,12312,3213,12323213,12321,312,3123,123123123,12312,312312312313124,14124412,412]
print(x.bit_length(),(10).bit_length())
for i in range(4194304):
    t = i+1#+1 range'te -1 oldugundan
    i.bit_length()
    #print("Sayi : {0} = {1} Bitlik".format(i,i.bit_length()))
print(t.bit_length())
#Float Metotlari
#as_integer_ratio - birbirine bolundugunde ilgili kayan noktali sayiyi veren iki adet tam sayi verir bize
print(z.as_integer_ratio())#9 sayisini 2 ye boldugumuzde 4.5 sayisini elde ederiz
#is_integer - Sayinin ondalik kismin da 0 harici sayinin olup olmadigini kontrol eder
print((12.0).is_integer() , (12.10).is_integer())
#Karmasik sayilarin metotlari
print(y.imag, y.real)
#Aritmetik fonksiyonlar
#abs - sayinin mutlak degerini bulur
print(abs(-12))
#divmod - bir sayının bir sayıya bölünmesi işleminde bölümü ve kalanı verir
print(divmod(12,2))
#max - list dizi icindeki en buyuk sayiyi verir
print(max(l))
#min
print(min(l))
#sum - dizi icindeki tum sayilari birbiriyle toplar
print(sum(l))
