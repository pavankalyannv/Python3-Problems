def seiveofpranthesis(n):
    prime = [True for i in range(0,n+1)]
    p = 2
    
    while(p*p <= n):
        if(prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    for i in range(2,n+1):
        if prime[i]:
            print(i,end=' ')
for i in range(0,int(input())):
    num = int(input())
    seiveofpranthesis(num)
