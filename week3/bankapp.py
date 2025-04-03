def credit(bal,value):
	bal+=value
	return bal
def debit(bal,value):
	bal-=value
	return bal
def checkbal(bal):
	print('total balance:',bal)
bal=0
bal=credit(bal,1400)
print('amount credited:',bal)
bal=debit(bal,900)
print('amount debited:',bal)
checkbal(bal)
