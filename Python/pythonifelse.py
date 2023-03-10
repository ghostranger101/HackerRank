#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = input()
    n = int(n)
    if n%2==0:
        if n>=2 and n<=5 and n==1:
            print("Not Weird")

        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
        


