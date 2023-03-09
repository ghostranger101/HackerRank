# Enter your code here. Read input from STDIN. Print output to STDOUT
def check(total,liss,lis):
    if liss[0] in lis:
        lis.remove(liss[0])
        total=total+int(liss[1])
    else:
        pass
    return total
        
if __name__ == '__main__':
    total=0
    x=input()
    lis=input().split()
    y=int(input())
    for i in range(y):
        liss=input().split()
        total=check(total,liss,lis)
        
    print(total)

