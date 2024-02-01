n=int(input("Enter a number:"))
r=0
c=n 
count=0
while(n!=0):
    d=n%10
    r=r*10+d
    count=count+1
    n=n//10
print(c," in words :")
while(count!=0):
    d=r%10
    if(d==0):
        print("Zero", end=" ")
    elif(d==1):
        print("One", end=" ")
    elif(d==2):
        print("Two", end=" ")
    elif(d==3):
        print("Three", end=" ")
    elif(d==4):
        print("Four", end=" ")
    elif(d==5):
        print("Five", end=" ")
    elif(d==6):
        print("Six", end=" ")
    elif(d==7):
        print("Seven", end=" ")
    elif(d==8):
        print("Eight", end=" ")
    elif(d==9):
        print("Nine", end=" ")
    r=r//10
    count=count-1