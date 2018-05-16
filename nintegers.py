num=input("enter the no:\n")

count=0

sum=1

if num<0:

    num=num+(-num)+(-num)
    while num>0:

        count=count+sum
 
        num=num//10
 
    print "the no. of integers is",count	

else:	
    
    while num>0:
   
        count=count+sum
     
        num=num//10
  
    print "the no. of integers is",count