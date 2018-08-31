#str.maketrans, translate
çeviri_tablosu = str.maketrans("a", "S")
metin = "a,b,c"
print(metin.translate(çeviri_tablosu))
#isalpha : karakter dizisinin ‘alfabetik’ olup olmadığını denetler
x = "Text"
y = "Text2"
print(x.isalpha(),y.isalpha())
#isdigit : karakter dizisinin sayısal’ olup olmadığını denetler
a = "3.14"
b = "123"
print(a.isdigit(),b.isdigit())
#isalnum : karakter dizisinin ‘alfanümerik’ olup olmadığını denetlememizi sağlar    
c = "12a3"
print(a.isalnum(),c.isalnum())
#isdecimal : karakter dizisinin ondalık sayı cinsinden olup olmadığını denetliyoruz
print(a.isdecimal(),b.isdecimal())
#isnumeric : karakter dizisinin nümerik olup olmadığını denetler
print(a.isnumeric(),b.isnumeric(),c.isnumeric())
#isspace : karakter dizisinin tamamen boşluklardan oluşup oluşmadığını denetleyebiliriz
h = ""
h2 = " "
print(h.isspace(),h2.isspace())
#isprintable : karakterin basılabilen bir karakter mi yoksa basılmayan bir karakter mi olduğunu söyler
print(a.isprintable(),"\n".isprintable())
