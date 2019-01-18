# 正则替换
import re
language = 'PythonC#JavaC#PHPC#'

def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'

r = re.sub('C#',convert,language)
print(r)

