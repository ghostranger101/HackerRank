import re

pat = "(?<=[^aeiou])([aeiou]{2,})[^aeiou]"
res = re.findall(pat, input(), flags=re.I)

print('\n'.join(res or ['-1']))

