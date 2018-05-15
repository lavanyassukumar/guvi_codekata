lower = input("enter the lower number : ")
upper = input('enter the upper number : ')
i=2
for num in range(lower,upper+1):
    if num>1 :
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print num
