def divide(x,y):
    try:
        result=x//y
    except ZeroDivisionError:
        print("Division by 0 not possible !!")
    else:
        print("Answer:",result)
    finally:
        print("Always executed !!")
        
        
divide(3,2)
divide(3,0)