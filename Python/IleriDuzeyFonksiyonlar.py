#Lambda Fonksiyonlari
fonk = lambda p1,p2:p1+p2
print(fonk(2,2))
fonk2 = lambda x:x % 2 == 0
print(fonk2(1152921504606846976))
#tkinter ile bir ornek
import tkinter
import tkinter.ttk as ttk
pen = tkinter.Tk()
btn = ttk.Button(text='merhaba', command=lambda: print('merhaba'))
btn.pack(padx=20, pady=20)
pen.mainloop()
#Ozyinelemeli fonksiyonlar - ic ice kullanmaktir
def azalt(s):
    if len(s) < 1:
        return s
    else:
        print(s)
        return azalt(s[1:])
print(azalt(input('deger:')))
#konu ozetlenmistir