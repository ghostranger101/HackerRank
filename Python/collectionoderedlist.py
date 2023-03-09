dict_obj={}

for i in range(int(input())):

    inp=(input().split())
    item=(' '.join(inp[:-1]))
    quant=inp[-1]

    if item in dict_obj.keys():
        dict_obj[item] = int(dict_obj[item])+int(quant)
    else:
        dict_obj[item] = quant
for i in dict_obj:
    print(str(i)+" "+str(dict_obj[i]))

