for i in range(int(input())):
    a=input().split()
    try:
        print(int(a[0])//int(a[1]))
    except Exception  as e:
        print("Error Code:",e)

