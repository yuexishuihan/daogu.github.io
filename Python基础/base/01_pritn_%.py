# a = input('请输入A的值\n')
# b = input('请输入B的值')
# a = int(a)
# b = int(b)
# print('a*b = ',a*b)
print('I\'m learning \"pyton\"')
print('''第一行内容
第二行内容
第三行内容''')
# cj = input()
# if cj >=80:
#     print('成绩优秀')
# elif cj >= 60：
#     print('成绩及格')
# else:
#     print('不及格')

n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n,f,s1,s2,s3,s4,sep = '\n')
print("包含中文的str")
print('Hello, %s'%'world')
print('Hi,%s,you have $%d.'%('Michael',1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Hello,{0},成绩提升了{1:.1f}%'.format('小明',17.125))
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

s1 = input('请输入小明去年成绩：\n')
s2 = input('请输入小明今年成绩：\n')
s1 = int(s1)
s2 = int(s2)
r  = (s2 - s1)/s1 * 100 
print('小明成绩提升的百分点为：%.1f%%'%r)