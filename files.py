 try:
	with open("test.txt") as file:
		data=file.read()

except:
	print("enter valid file")
  
print (data)
