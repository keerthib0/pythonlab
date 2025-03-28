n=input("enter a character:-")[0]
print(n)
if(n.islower()):
     print(n,' is lowercase')
elif(n.isupper()):
     print(n,'is uppercase')
elif(n.isdigit()):
     print(n,' is a digit')
else:
     print(n,' is a special character')
