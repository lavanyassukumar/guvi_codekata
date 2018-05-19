num=raw_input("enter a number to be reverse :  ")
if isinstance(num,str):
    print "enter a no. not a string"
else:
    sum=0
    rnum=0
    while num>0:
        rem=num%10
        sum=sum*10+rem
        rnum=rnum*10+rem
        num=num/10
    print 'the reversed no. is',rnum
