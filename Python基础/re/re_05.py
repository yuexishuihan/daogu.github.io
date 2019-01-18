#数量词
import re
a = 'python 1111java678php'
r = re.findall('[a-z]{3,6}',a)
#贪婪与非贪婪(?)
print(r)