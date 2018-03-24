N=int(input("enter N:"))
Q=int(input("enter Q:"))
N=N+1
if(N%2==0):
    for i in range(N,Q,2):
        print i
else:
    N+=1
    for i in range(N,Q,2):
        print i

