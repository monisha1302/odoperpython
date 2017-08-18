def func(s):
	d=dict(e.split('=') for e in s.split(';'))
	return d;
s='a=b; c=d; e=f; g=h'
print func(s);
