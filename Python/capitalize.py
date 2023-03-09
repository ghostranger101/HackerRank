
def up(i):
    return i.upper()
def solve(s):
    lis=list(s)
    for i in range(0,len(lis)):
        if i==0:
            lis[i]=up(lis[i])
        elif lis[i]==' ':
            lis[i+1]=up(lis[i+1])
        else:continue
    return "".join(lis)
            


