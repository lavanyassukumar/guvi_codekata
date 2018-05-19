N=int(raw_input('enter the no. : '))
i=1
sum=1
if(20>N>0):
    while (i<=N):
        sum=sum*i
        i+=1
    print(sum)
else:
    print('enter a num below 20')
    
