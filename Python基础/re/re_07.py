#边界匹配 
# ^从字符串开头匹配 
# $从字符串末尾匹配
import re
qq = '1000000001'
# 4~8
r = re.findall('^\d{4,8}$',qq)
print(r)