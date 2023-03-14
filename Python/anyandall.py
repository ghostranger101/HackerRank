n = int(input())
values = list(map(int, input().split()))
print(any( str(i) == str(i)[::-1] for i in values) and all(i>0 for i in values))

