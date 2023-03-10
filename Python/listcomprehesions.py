if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    def rang(p):  
        li=[]  
        for i in range(p+1):
            li.append(i)
        return li
    list=[]
    valx=rang(x)
    valy=rang(y)
    valz=rang(z)
    for i in valx:
        for j in valy:
            for k in valz:
                li=[i,j,k]
                if i+j+k!=n:
                    if li in list:
                        pass
                    else:
                        list.append(li)
    print(list)

