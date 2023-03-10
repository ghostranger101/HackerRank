if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    arr = [int(arr) for arr in arr]
    arr.sort(reverse=True)
    a=arr[0]
    def check(arr,a):
        for i in arr:
            if i==a:p=True
            else:p=False
        for i in arr:
            p=0
            if p==True:
                print(a)
            elif a>i: 
                print(i)
                break
            else:
                pass
    check(arr,a)

