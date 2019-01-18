score = int(input('请输入你的成绩：\n'))
if score >=80:
    cj = '优秀'
elif score >=60:
    cj = '及格'
else:
    cj = '不及格'
print('你的成绩为:',score)
print(cj)

height = float((input('身高=')))
weight = float(input('体重='))
bmi=weight/(height**2)
if bmi < 18.5:
    print('过轻')
elif 18.5 < bmi < 25:
    print('正常')
elif 25 < bmi < 28:
    print('过重')
elif 28 < bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')

