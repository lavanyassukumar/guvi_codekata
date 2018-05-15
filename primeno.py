num=input("enter the number to check whether it is prime or not : ")
i=2
if num>1:
    for i in range(2,num):
            if (num%i==0):
                    print num,' no, not a prime '
                    break
    else:
            print num,' yes prime'
else:
        print num,' no, not a prime '
