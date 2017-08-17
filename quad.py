import math
global r1, r2, ipart, rpart
print("Enter coeff of x^2, x and const")
a= float(input("a="))
b= float(input("b="))
c= float(input("c="))
d= (b*b)-(4*a*c)
if(d==0):
	print("Roots are equal \n")
	r1=r2= (-b)/(2*a)
	print("r1=r2=", r1)
 if(d>0):
	print("roots are real \n")
	r1=(-b-(math.sqrt(-d)))/(2*a)
	r2=(-b+(math.sqrt(-d)))/(2*a)
	print("r1=", r1, "r2=", r2)
 if(d<0):
	print("roots are imaginary")
	rpart=(-b)/(2*a)
	ipart=(math.sqrt(-d))/(2*a)
	print("r1=", rpart, "+", ipart, "r2", rpart, "-", ipart)
