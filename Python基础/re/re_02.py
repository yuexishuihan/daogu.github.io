import re
a = 'C0C++7JAava8C#9Python6Javascript'
r = re.findall('\d',a) #正则表达式匹配int
print(r)
# 'Python'普通字符
# '\d'元字符