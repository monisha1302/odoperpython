def fib():
	a,b=0,1
	while 1:
		yield a
		a,b = b, a+b

		
a=10
b=fib()
b.next()
for i in range(a):
	print b.next()
