def createlist(l,n):
    print('enter elements of list:-')
    for i in range(n):
        temp=int(input())
        l.append(temp)
    return l
n1 = int(input('enter the limit of list a:-'))
n2 = int(input('enter the limit of list b:-'))
n3 = int(input('enter the limit of list c:-'))
alist = []
blist = []
clist = []
alist1=createlist(alist,n1)
print(alist1)
blist1=createlist(blist,n2)
print(blist1)
clist1=createlist(clist,n3)
print(clist1)
