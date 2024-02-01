#Dictionary Program
dic={1:"A", 2:"B", 3:"C"}
dict=dic.items()
for i in dict:
    print(i)
a=int(input("Enter the key to access:"))
print("The value of enetered key:",dic[a])
print(dic.get(1))
dic1={1:"E", 2:"F", 3:"G"}
dic.update(dic1)
print("Value after updating:",dic)
print("Length of the dictionary:",len(dic))