def conv(d):
	return ",".join("=".join((k, str(v))) for k, v in sorted(d.items()))

d=dict(a=1, b=2, c=3)
conv(d)
