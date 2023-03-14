cube = lambda x: pow(x,3) 
lis=[0,1]
def fibonacci(n):
    if n==0:
        lis.clear()
    elif n==1:
        lis.clear()
        lis.append(0)
    else:
        for i in range(1,n-1):
            ans=int(lis[i])+int(lis[i-1])
            lis.append(ans)
    return lis

