def fact(x):
    factorial=1
    while(x>0):
        factorial=factorial*x
        x=x-1
    return factorial


n=int(input("Enter a number:"))
print("Factorial of the number is:",fact(n))