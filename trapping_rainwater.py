https://practice.geeksforgeeks.org/problems/trapping-rain-water/

#code
for i in range(int(input())):
    size = int(input())
    arr = list(map(int,input().split()))
    lmax = arr[0]
    rmax = max(arr[1:])
    count = 0
    for i in range(size):
      if arr[i]>lmax:
        lmax=arr[i]
      if ((arr[i]==rmax) and (i<size-1)):
        rmax = max(arr[i+1:])
      m = min(lmax,rmax)
      if arr[i]<=m:
        count += max(m-arr[i],0)
    print(count)
