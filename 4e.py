def double(a):
    d=a+a 
    return d    

list=[11,22,33,44,55,66,77,88,99,100]
print("Normal list:")
print(list)
print("Doubled list:")
s=len(list)
for i in range(0,s):
    n=double(list[i])
    print(n)    