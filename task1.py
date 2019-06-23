count=1
instr=input("enter the string")+' '
a=instr
j=0
s=" "
for i in instr:
    if(j<len(instr)-1):
        if(a[j] == a[j+1]):
            count+=1
            j+=1
        else:
            
            s+=a[j]+str(count)
            count=1
            j+=1
print(s)
            

