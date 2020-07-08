https://practice.geeksforgeeks.org/problems/inverse-permutation/

#code
for i in range(int(input())):
    size = int(input())
    li = [0]*size
    arr = list(map(int,input().split()))
    for index,value in enumerate(arr):
        li[value-1] = index+1 
    a=' '.join(map(str,li))
    print(a)
    
    
    
