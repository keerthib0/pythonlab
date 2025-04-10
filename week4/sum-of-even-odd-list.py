def createlist(l,n):
    l=[]
    print('enter elements of list:-')
    for i in range(n):
        temp=int(input())
        l.append(temp)
    return l
def evensum(l):
    sum=0
    for j in range(len(l)):
        if (j%2==0):
            sum+=l[j]
    return sum
def oddsum(l):
    sum=0
    for j in range(len(l)):
        if (j%2!=0):
            sum+=l[j]            
    return sum        
alist = []
blist = []
clist = []
n1 = int(input('enter the limit of list a:-'))
alist=createlist(alist,n1)
print(alist)
x,x1=(evensum(alist)),(oddsum(alist))
print(x,x1)
n2 = int(input('enter the limit of list b:-'))
blist=createlist(blist,n2)
print(blist)
y,y1=evensum(blist),oddsum(blist)
print(y,y1)
n3 = int(input('enter the limit of list c:-'))
clist=createlist(clist,n3)
print(clist)
z,z1=evensum(clist),oddsum(clist)
print(z,z1)
a=((x+y+z)*(x1+y1+z1))
print('Multiplication of even sum and odd sum:-',a)
