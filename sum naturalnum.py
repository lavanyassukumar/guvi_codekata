sum=0
i=1
N=int(input("enter the value of N : "))
if(N==0):
    print("enter a natural no.")
else:
    while i<=N :
        sum=sum+i
        i+=1
    print(sum)
