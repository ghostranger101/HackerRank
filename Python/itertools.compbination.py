from itertools import combinations
def dis(lis):
    for i in lis:
        print("".join(i))
ans=[]
string,n=input().split()
for i in range(1,int(n)+1):
    dis(list(combinations(sorted(string),i)))

