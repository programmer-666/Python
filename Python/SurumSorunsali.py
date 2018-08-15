import sys
_2x_metni = """
Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı."""
_3x_metni = "Programa hoşgeldiniz."
if sys.version_info.major < 3:
print(_2x_metni)
else:
print(_3x_metni)
#Farklı sürümler için.. konu özetlenmiştir