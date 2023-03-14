lis=set(input().split())
final=[]

for i in range(int(input())):
    m=set(input().split())
    z = lis.issuperset(m)
    final.append(z)
for i in final:
    if i==True:
        ans=1
    else:
        ans=0
        break
if ans==1:print(True)
else:print(False)

