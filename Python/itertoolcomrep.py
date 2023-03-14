from itertools import combinations_with_replacement
string,n=input().split()
for i in list(combinations_with_replacement(sorted(string),int(n))):
    print("".join(i))
    

