import re
a = 'C|C++|JAVA|C#|Python|Javascript'

print(a.index('Python')>1)

print('Python' in a)

r = re.findall('Python',a)
if len(r) > 0:
    print('字符串包含Python')
# print(r)