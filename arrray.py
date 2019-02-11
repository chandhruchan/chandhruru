n=int(input())
k=int(input())
a=[]
summ=0
for i in range(1,n+1):
    a.append(i)
for j in range(0,k+1):
    summ=summ+a[j]
print(summ) 
