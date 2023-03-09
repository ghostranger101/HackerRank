if __name__=='__main__':
    lis1=input().split()
    lis2=input().split()
    final=''
    for i in lis1:
        for j in lis2:
            a=((int(i),int(j)))
            print(a, end =" ")
    print(final)

