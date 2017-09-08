class fib():
   def __init__(self):
     self.a,self.b=0,1
   def __iter__(self):
     return self
   def __next__(self):
     if count==1: 
        return self.a
     self.a,self.b=self.b,self.a + self.b
     return self.a
 
 count=1
 n=10
 x=fib()
 iter(x)
 for i in x:
   print(i)
   count+=1
