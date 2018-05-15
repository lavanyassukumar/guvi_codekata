num=int(raw_input('enter the number : '))
sum=0
rnum=0
rem=0
a=num
while num!=0:
    rem=num%10
    sum=sum*10+rem
    rnum=rnum*10+rem
    num=num/10
if(a==rnum):
    print('palindrom')
else:
    print('not palindrome')
