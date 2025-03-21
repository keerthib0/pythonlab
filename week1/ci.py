Compound Interest Python Code:-

p=int(input("enter principal amount:-")) 
t=int(input("enter time:-"))
r=int(input("enter interest rate:-"))
a=p*(1+r/100)**t
ci=a-p
print(round(ci,2))
