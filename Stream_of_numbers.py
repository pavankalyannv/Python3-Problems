#code
def average(a):
    b=[]
    for i in range(len(a)):
        if i==0:
            b.append(a[i])
        else:
            c=sum(a[:i+1])
            c=c//(i+1)
            
            b.append(c)
    return b        
s=int(input(""))   
x=[]
for i in range(s):
    n=int(input(""))
    a = list(map(int,input().split()))
    x=(average(a))
    res = ' '.join(map(str,x))
    print(res)
        
        
        
