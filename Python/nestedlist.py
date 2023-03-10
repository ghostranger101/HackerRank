if __name__ == '__main__':
    sc=[]
    li=[]
    
    def check(li,sc):
        x = min(sc)
        pi=[]
        for i in sc:
            if i != x:
                pi.append(i)
        # print(pi)
        # maxV=0
        # for i in sc:
        #     if i == maxV:
        #         sc.remove(i)
        # print(sc)
        x=min(pi)
        sc.clear()
        for i in li:
            for j in range(1):
                if x in i:
                    sc.append(i[0])
                else:
                    pass
                
 
        x=sorted(sc)
        for i in x:    
            print(i) 
        
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name,score])
        sc.append(score)
    check(li,sc)    

