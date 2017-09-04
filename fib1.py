def fib(x):
    results = []
    i=0
    t1 = 0
    t2 = 1
    while i <= x-1:
        results.append(t1)
        i += 1
        nextTerm = t1 + t2
        t1 = t2
        t2 = nextTerm
    return results

x=6
print fib(x)
