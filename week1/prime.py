Prime Number python code:-

n=int(input("enter a number:-"))
flag=0
for i in range(2,n): //2 because its the smallest prime number//
      if(n%i==0):
          flag=1
          print("not a prime number")
          break;
if(flag==0):
     print("is a prime number")
