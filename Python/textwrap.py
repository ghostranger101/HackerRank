def wrap(string, max_width):
    k=0
    j=max_width
    l=len(string)
    li=''
    for i in range(int(l/max_width)+1):
        li=li+string[k:j]
        k=k+max_width
        j=j+max_width
        if j>l:j=l
        li=li+'\n'
    return li


