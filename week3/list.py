def printlist(elements):
    for i in elements:
    	print(i)
elements = []
limit = int(input('enter the no. of elements:-'))
for i in range(limit):
    elem=int(input())
    elements.append(elem)
printlist(elements)
