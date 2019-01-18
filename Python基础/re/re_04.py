# 概括字符集
import re
a = 'python111java&678php'
r = re.findall('[A-Za-z0-9_]') #等同于单词字符集'\w'
                               #'\W'非单词字符：&、空格 、回车\n、制表符\t
                               #'\s'空白字符