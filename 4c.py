def double(a):
    d=a+a 
    return d 
  
n1=int(input("Enter a number:"))
n2=double(n1)
l=lambda a,b : a + b
print("Sum using lambda():",l(n1,n2))