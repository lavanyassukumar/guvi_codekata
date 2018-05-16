start_num=input("enter the starting no:")
end_num=input("enter the ending no:")
sum=1
count=0
p=end_num-start_num
while p>0:
    count=count+sum
    p=p//10
if(count==3):
    for num in range(start_num,end_num+1):
        if num<=end_num :
            y=num
            a=num/100
            b=num%100
            c=b/10
            d=b%10
            l=a*a*a
            m=c*c*c
            n=d*d*d
            s=l+m+n
            if (y==s) :
                print(s,"it is an armstrong no.")
            else:
                num+=1
else:
    print ("the given starting and ending nos should be in three digit")
