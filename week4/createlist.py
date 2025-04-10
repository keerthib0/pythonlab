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
alist=createlist(alist,n1)
print(alist)
blist=createlist(blist,n2)
print(blist)
clist=createlist(clist,n3)
print(clist)

