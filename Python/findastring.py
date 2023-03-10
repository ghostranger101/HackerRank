def count_substring(string, sub_string):
    count=0
    t=len(sub_string)
    for i in range(len(string)):
        comstring=string[i:i+t]
        if comstring==sub_string:
                count=count+1
        else:continue
            
    return count


