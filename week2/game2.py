import random
n=random.randint(0,100)
count=5
while(count>0):
     x=int(input("guess the number:- "))
     if(x<n):
          print("too low!!!")
     elif(x>n):
          print("too high!!")
     else:
          print("Yayyy!!!")
          break;
     count-=1
print("     You lost!!")
