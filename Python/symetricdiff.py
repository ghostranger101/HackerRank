n=int(input())
eng=set(input().split())
m=int(input())
fre=set(input().split())
print(len(eng.symmetric_difference(fre)))

