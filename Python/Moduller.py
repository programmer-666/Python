import os #ile modul ice aktarilir
print(os.name)#windows=nt , gnu/linux=posix
#os.makedirs('DenemeDosyasi')#dizin olusturur , var olan bir dosyayi tekrar olusturamazsiniz...
print(os.getcwd())#buldugu dizini gosterir
#farklisekilde ice aktarma 
import subprocess as sub
sub.call('notepad.exe')
import webbrowser as web
web.open('www.google.com')
#diger
from distutils import sysconfig
print(sysconfig.get_python_lib())