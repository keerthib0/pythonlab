with open('harry_potter.txt','r') as f:
  hi=f.read()


splitted_data=hi.split('\n')


title=splitted_data[0]
title


author=splitted_data[-1]
author


titleyear=splitted_data[1:-1]
titleyear


D={}
i=0
for i in range(len(titleyear)):
  a=title + ' ' +str(i+1)
  D[a]=None
D


titlelist=[]
yearlist=[]
for i in titleyear:
  title=i.split('(')[0].strip()
  titlelist.append(title)
  years=i.split('(')[1][:-1]
  yearlist.append(years)
print(titlelist)
yearlist


i=0
for key in D:
  D[key]={"title":titlelist[i],"year":yearlist[i],"author":author}
  i+=1
D


for i in D:
  print(i,D[i])
