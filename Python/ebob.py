import os
os.system("cls")
while True:
	def ebob(a,b):
		while b:
			a,b=b,a%b;
		return a;
	def ebobb(*args):
		return reduce(ebob, args)
	def ekok(a,b):
		return a*b/ebob(a,b);
	def ekokk(*args):
    		return reduce(ekok, args)

	x = int(input("1 : "))
	y = int(input("2 : "))

	print("Ebob : ",ebob(x,y),"Ekok : ",ekok(x,y))
	input()
	os.system("cls")