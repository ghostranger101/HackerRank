def check(s):
    li=[0,0,0,0,0]
    for i in s:
        if i.isalnum()==True:
            li[0]=li[0]+1
        else:pass
        if i.isalpha()==True:
            li[1]=li[1]+1
        else:pass
        if i.isdigit()==True:
            li[2]=li[2]+1
        else:pass
        if i.islower()==True:
            li[3]=li[3]+1
        else:pass
        if i.isupper()==True:
            li[4]=li[4]+1
        else:pass
    for i in li:
        if i!=0:print(True)
        else:print(False)
if __name__ == '__main__':
    s = input()
    check(s)

