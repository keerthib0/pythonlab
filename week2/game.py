import random
n=random.randint(0,14)
while(True):
     x=int(input("guess the number"))
     if(x<n):
          print("too low!!!")
     elif(x>n):
          print("too high!!")
     else:
          print("Yayyy!!!")
