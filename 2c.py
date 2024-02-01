ll=int(input("Enter lower limit:"))
ul=int(input("Enter upper limit:"))
flag=0
n=0
for i in range(ll,ul+1):
    n=i
    for j in range(2,i):
        if n%j==0:
            flag=flag+1
    if flag==0:
        print(n," is prime !!")