n=int(input())
lis=set(input().split())
to=0
for i in range(int(input())):
    cmd=input().split()
    fre=set(input().split())
    if cmd[0]=="intersection_update":lis.intersection_update(fre)
    elif cmd[0]=="update":lis.update(fre)
    elif cmd[0]=="difference_update":lis.difference_update(fre)
    elif cmd[0]=="symmetric_difference_update":lis.symmetric_difference_update(fre)
    else:pass
for i in  lis:
    to=to+int(i)
print(to)

