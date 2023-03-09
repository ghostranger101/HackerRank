def minion_game(string):
    kevin=stuart=0
    length=len(string)
    total=pow(2,length)-1
    for i in range(length):
        if string[i] in {'A','E','I','O','U'}:
            kevin=kevin+(length-i)
        else:
            stuart=stuart+(length-i)    
    if kevin>stuart:print("Kevin "+str(kevin))
    elif kevin==stuart:print("Draw")
    else: print("Stuart "+str(stuart))
    

