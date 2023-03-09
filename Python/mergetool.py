def conv(string):
    p=""
    for i in string:
        if i not in p:
            p=p+i
        else:
            pass
    print(p)
def merge_the_tools(string, k):
    val=int(len(string)/k)
    for i in range(0,len(string),k):
        conv(string[i:i+k])
        i=i+k


