# * 匹配0次或者无限多次
# + 匹配1次或者无限多次
# ? 匹配0次或者1次
import re
a = 'pytho0python1pythonn2'
r = re.findall('python?',a)