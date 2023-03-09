import re

for i in range(int(input())):
    inp=input()
    try:
        re.compile(inp)
        print('True')
    except re.error:
        print('False')

