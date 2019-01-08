varA=input("enter the a")
varB=input("enter the b")
if(varA.isnumeric() and varB.isnumeric()):
	if(varA>varB):
		print("a is bigger")
	elif(varA<varB):
		print("a is smaller")
	else:
		print("equal")
else:
	print("string involved")
	if(len(varA)>len(varB)):
		print("a is bigger")
	elif(len(varA)<len(varB)):
		print("a is smaller")
	else:
		print("equal")
	