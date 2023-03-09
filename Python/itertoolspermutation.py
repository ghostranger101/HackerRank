from itertools import permutations
if __name__ == '__main__':
    l=input().split()
    lis=l[0]
    n=l[1]
    final=""
    val=permutations(lis,int(n))
    val=sorted(val)
    for i in val:
        for j in i:
            final=final+str(j)
        print(final)
        final=""

