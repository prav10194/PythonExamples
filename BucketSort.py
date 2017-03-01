def bucketSort(a):
    n=10 #number of buckets
    bucket=[0]*n
    for a1 in a:
        #print(a1)
        if not bucket[int(n*a1)]: #if bucket is empty. It will be 0 if not yet initialized. 
            blist=[a1]
            bucket[int(n*a1)]=blist
        else:
            blist=bucket[int(n*a1)]
            blist.append(a1)
            bucket[int(n*a1)]=blist

    for b in bucket:
        if b!=0:
            insertion_sort(bucket)
            
    finalBucket=[]
    for b in bucket:
        if b!=0:
            finalBucket+=b
            #t1.append(b1)

    return finalBucket

def insertion_sort(a): #not exactly an insertion sort
    for i in range(1,len(a)):
	#print("In loop"+str(i))
        for j in range(i-1,-1,-1):
            #print("j: "+str(j))
            if a[j]>a[j+1]:
                #print(str(a[j])+"\t"+str(a[j+1]))
                temp=a[j+1]
                a[j+1]=a[j]
                a[j]=temp
    return a

print(bucketSort([0.2,0.1,0.5,0.55,0.56,0.11,0.22,0.7,0.25,0.4]))
