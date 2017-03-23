d=[1,5,10,25,100]  #initial denominations of money

#sort in descending order
for i in range(0,len(d)):
	for j in range(0,len(d)-1):
		if d[j]<d[j+1]:
			t=d[j]
			d[j]=d[j+1]
			d[j+1]=t

i=0 #initialize loop variable to 0
r=34 #the money you want to get the change of

while(i<len(d)):
	if r>=d[i]:
		print(d[i])
		r=r-d[i]
		i-=1 #loop back again
	else:
		i+=1 #loop forward
