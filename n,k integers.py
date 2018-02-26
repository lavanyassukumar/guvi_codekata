N=int(input('enter the value of N : '))
k=int(input('enter the value of k : '))
varcount=1
sum=0
i=1
print('The N integers is')
while varcount<=N :
    print(varcount)
    varcount+=1
if (k>N):
    print("enter k within the N integers")
else:
    while i<=k:
        sum=sum+i
        i+=1
    print 'The sum of first k integers is',sum

