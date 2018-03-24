a=int(input("enter a:"))
b=int(input("enter b:"))
s=0
if (a<100000 and b<100000):
    print 'a=',a
    print 'b=',b
    a=a+1
    if(a%2==0):
        a+=1
        for i in range(a,b,2):
            print i
    else:
        for i in range(a,b,2):
            print i
else:
    print ("enter a&b below 100000")


