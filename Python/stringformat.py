def print_formatted(number):
    b=int(len(bin(number)))-2
    for i in range(1,number+1):
        print(str(i).rjust(b," ")+" "+str(oct(i))[2:].rjust(b," ")+" "+str(hex(i))[2:].upper().rjust(b," ")+" "+str(bin(i))[2:].rjust(b," "))
    
    # your code goes here


