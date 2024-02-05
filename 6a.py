thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[3:6])
print(thislist[2:])
print(thislist[3:6])
for i in range(0,len(thislist)):
    flag=0
    if(thislist[i]=="apple"):
        flag=1
        break
if(flag==1):
    print("Present")
else:
    print("Not Present")
thislist[1]="blackcurrant"
thislist[2]="watermelon"
thislist.append("guava")
print(thislist)