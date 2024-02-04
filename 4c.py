def even(a):
    if (a%2==0):
        return 1
    else:
        return 0
    
    

list=[11,22,33,44,55,66,77,88,99,100]
s=len(list)
for i in range(0,s):
    flag=0
    n=list[i]
    flag=even(n)
    if(flag==1):
        print(n)