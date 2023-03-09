v=int(input())
lis=(input().split()).index('MARKS')
total=0
for i in range(v):
    marks=int(input().split()[lis])
    total= total+marks
print(float(total/v))
    

