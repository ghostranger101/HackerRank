def average(array):
     # Introduction to Sets in Python - Hacker Rank Solution START
    sum_array = sum(set(array))
    len_array = len(set(array))
    output = sum_array/len_array
    return output;


