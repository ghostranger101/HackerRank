input()
a=set(map(int, input().split()))
input()
b=set(map(int, input().split()))
c=a.union(b)
d=a.intersection(b)
e=sorted(list(c.difference(d)))
for i in e:print(i)

