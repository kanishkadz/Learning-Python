ll=int(input("Enter lower limit:"))
ul=int(input("Enter upper limit:"))
for n in range(ll, ul+1):
    if n>1:
        for i in range(2,n):
            if(i==n):
                i=n
                break
            if(n%i==0):
                n=n-1
print("Value of highest prime is:",i)