num=input("enter the no:\n")
count=0
sum=1
p=num
while num>0:
    count=count+sum
    num=num//10

if(count==3):
    y=p
    a=p/100
    b=p%100
    c=b/10
    d=b%10
    l=a*a*a
    m=c*c*c
    n=d*d*d
    s=l+m+n
    if (y==s) :
        print("it is an armstrong no.")
    else:
        print("it is not an armstrong no.")
else:
    print ("please enter a three digit no.")
