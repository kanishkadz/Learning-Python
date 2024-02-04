def Addition(x1,x2):
    print("Sum is:",x1+x2)
    
def Subtraction(x1,x2):
    print("Difference is:",x1-x2)
    
def Multiplication(x1,x2):
    print("Product is:",x1*x2)
    
def Division(x1,x2):
    print("Factor is:",x1//x2)

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print("-: M E N U :-")
print("1 --> Addition")
print("2 --> Subtraction")
print("3 --> Multiplication")
print("4 --> Division")
ch=int(input("Enter your choice:"))
if(ch==1):
    Addition(x,y)
elif(ch==2):
    Subtraction(x,y)
elif(ch==3):
    Multiplication(x,y)
elif(ch==4):
    Division(x,y)
else:
    print("Wrong choice !!")