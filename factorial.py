fac=int(raw_input('enter the no. : '))
i=1
sum=1
if(fac>0):
    while (i<=fac):
        sum=sum*i
        i+=1
    print(sum)
else:
    print('enter a valid no.')