Prime Number python code:-

n=int(input("enter a number:-"))
for i in range(2,n):
      if(n%i==0):
       print("not a prime number")
       break;
else:
     print("is a prime number")
