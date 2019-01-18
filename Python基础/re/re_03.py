import re
s = 'abc,acc,adc,aec,afc,ahc'

r = re.findall('a[cf]c',s)
# r = re.findall('a[^cf]c',s)  取反
# r = re.findall('a[c-f]c',s)  c到f
print(r)