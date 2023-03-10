if __name__ == '__main__':
    lis=[]
    N = int(input())
    def insert(lis,i,e):
        lis.insert(i, e)
    def pri(lis):
        print(lis)
    def remove_e(lis,e):
        lis.remove(e)
    def append_e(lis,e):
        lis.append(e)
    def sort(lis):
        lis.sort(reverse=False)
    def pop(lis):
        lis.pop(-1)
    def reverse(lis):
        lis.reverse()
    for i in range(N):
        com=input().split()
        # print(com)
        for x in com:
            if 'insert' in x:insert(lis,int(com[1]),int(com[2]))
            elif 'print' in x:pri(lis)
            elif 'remove' in x:remove_e(lis,int(com[1]))
            elif 'append' in x:append_e(lis,int(com[1]))
            elif 'sort' in x:sort(lis)
            elif 'pop' in x:pop(lis)
            elif 'reverse' in x:reverse(lis)
            else:pass

