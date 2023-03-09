count=[]
for i in range(int(input())):
    char=input()
    if char in count:pass
    else:count.append(char)
print(len(count))

