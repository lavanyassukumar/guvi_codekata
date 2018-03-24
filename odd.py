a=int(input("enter a:"))
b=int(input("enter b:"))
s=0
if (a<100000 and b<100000):
    print 'a=',a
    print 'b=',b
    s=a+1
    if(s%2==0):
        s+=1
        for i in range(s,b,2):
            print i
    else:
        for i in range(a,b,2):
            print i
else:
    print ("enter a&b below 100000")


